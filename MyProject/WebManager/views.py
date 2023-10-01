import requests
from django.shortcuts import render
import json


def index(request):
    return render(request, 'WebManager/login.html', {'title': 'Главная сайта'})


def registration_form(request):
    return render(request, 'WebManager/registration.html')


def registration(request):
    def send_post_request(url, data):
        response = requests.post(url, json=data)
        if response.status_code == 201:
            result = response.status_code
            return result
        else:
            print(f"Request failed with status code {response.status_code}")

    flag = 0
    # Получаем данные с формы
    login = request.GET['login']
    password = request.GET['password']
    first_name = request.GET['first_name']
    last_name = request.GET['last_name']
    birth_date = request.GET['birth_date']
    if birth_date != '':
        data_users = {
                        "login": login,
                        "password": password,
                        "first_name": first_name,
                        "last_name": last_name,
                        "birth_date": birth_date
                      }
    else:
        data_users = {
                        "login": login,
                        "password": password,
                        "first_name": first_name,
                        "last_name": last_name,
                      }

    # Отправляем данные на сервер
    create_user = send_post_request("http://127.0.0.1:8000/MyAPI/api/register/", data_users)
    print(create_user)
    print(type(create_user))
    if create_user == 201:
        flag = 1
        return render(request, 'WebManager/info2.html', {'flag': flag})
    else:
        flag = 0
        return render(request, 'WebManager/info2.html', {'flag': flag})


def account(request):
    # Get function
    def send_get_request(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code {response.status_code}")

    flag = 0
    # Получаем данные с формы
    login = request.GET['login']
    password = request.GET['password']
    # Получаем данные о пользователе
    data_user_msg = send_get_request("http://127.0.0.1:8000/MyAPI/api/login/" + login + "/" + password)
    if not data_user_msg:
        flag = 1
        return render(request, 'WebManager/info.html', {'info_error': flag})
    else:
        msg = json.dumps(data_user_msg[0])
        data_user = json.loads(msg)
        # Получаем данные о всех событиях
        data_tasks = send_get_request("http://127.0.0.1:8000/MyAPI/api/events/")
        # Получаем данные о событиях пользователя
        data_user_tasks = send_get_request("http://127.0.0.1:8000/MyAPI/api/find/"+str(data_user.get('id')))
        return render(request, 'WebManager/account.html',
                  {'title': 'Главная сайта', 'data_tasks': data_tasks, 'data_user': data_user,
                   'data_user_tasks': data_user_tasks})


# Функция для просмотра выбранного пользователем события
def select_task(request, login, x):
    def send_get_request(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code {response.status_code}")

    # проверка является ли пользователь создателем
    def compare_dict(dict1, dict2):
        flag = 0
        if dict1.get('id') == dict2.get('creator'):
            flag = 1
            return flag
        else:
            flag = 0
            return flag

    # проверка есть ли пользователь в участниках события
    def compare_dict2(dict1, dict2):
        flag2 = 0
        if dict1.get('id') in dict2.get('participants'):
            flag2 = 1
            return flag2
        else:
            flag2 = 0
            return flag2

    # Получаем данные о всех событиях
    data_user = send_get_request("http://127.0.0.1:8000/MyAPI/api/list_user/" + login)
    # Получаем данные о событиях пользователя
    data_select_task = send_get_request("http://127.0.0.1:8000/MyAPI/api/add/" + x)
    # Получаем данные о всех событиях
    data_tasks = send_get_request("http://127.0.0.1:8000/MyAPI/api/events/")
    # Получаем данные о событиях пользователя
    data_user_tasks = send_get_request("http://127.0.0.1:8000/MyAPI/api/find/" + str(data_user.get('id')))
    flag = compare_dict(data_user, data_select_task)
    flag2 = compare_dict2(data_user, data_select_task)
    list_participants = data_select_task.get('participants')
    end_list = []
    for el in list_participants:
        data_user_participants = send_get_request("http://127.0.0.1:8000/MyAPI/api/list_user/" + str(el))
        end_list.append(data_user_participants)
    print(end_list)
    return render(request, 'WebManager/look_task.html',
                  {'title': 'Страница событий', 'data_tasks': data_tasks, 'data_select_task': data_select_task,
                   'data_user': data_user, 'data_user_tasks': data_user_tasks, 'flag': flag, 'flag2': flag2, 'list_participants': end_list})


# Функция для принятие участия пользователем в событии
def add_participant(request):
    def send_patch_request(url, data):
        response = requests.patch(url, json=data)
        if response.status_code == 201:
            result = response.status_code
            return result
        else:
            print(f"Request failed with status code {response.status_code}")

    def send_get_request(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code {response.status_code}")

    flag = 0
    user_id = int(request.GET['user_id'])
    list_participant = json.loads(request.GET['list_participant'])
    select_task_id = request.GET['select_task_id']
    data_user = send_get_request("http://127.0.0.1:8000/MyAPI/api/list_user/" + str(user_id))

    if user_id not in list_participant:
        print("нет")
        list_participant.append(user_id)
        list_participant.sort()

        json_data = dict({"participants": list_participant})
        url = "http://127.0.0.1:8000/MyAPI/api/add/" + select_task_id + "/"

        data_participant = send_patch_request(url, json_data)
        if data_participant == 201:
            flag = 1
            return render(request, 'WebManager/test2.html', {'data_user': data_user, 'flag': flag, 'select_task_id': select_task_id})
    else:
        flag = 0
        print("да")
    return render(request, 'WebManager/test2.html', {'data_user': data_user, 'flag': flag, 'select_task_id': select_task_id})


# Функция для отмены участия пользователем в событии
def no_participant(request):
    def send_patch_request(url, data):
        response = requests.patch(url, json=data)
        if response.status_code == 201:
            result = response.status_code
            return result
        else:
            print(f"Request failed with status code {response.status_code}")

    def send_get_request(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code {response.status_code}")

    flag = 0
    user_id = int(request.GET['user_id'])
    list_participant = json.loads(request.GET['list_participant'])
    select_task_id = request.GET['select_task_id']
    data_user = send_get_request("http://127.0.0.1:8000/MyAPI/api/list_user/" + str(user_id))

    if user_id in list_participant:
        list_participant.sort()
        list_participant.remove(user_id)

        json_data = dict({"participants": list_participant})
        url = "http://127.0.0.1:8000/MyAPI/api/add/" + select_task_id + "/"

        data_participant = send_patch_request(url, json_data)
        if data_participant == 201:
            flag = 1
            return render(request, 'WebManager/test3.html', {'data_user': data_user, 'flag': flag, 'select_task_id': select_task_id})
    else:
        flag = 0
    return render(request, 'WebManager/test3.html', {'data_user': data_user, 'flag': flag, 'select_task_id': select_task_id})


# Функция для удаления пользователем события
def del_participant(request):
    def send_delete_request(url):
        response = requests.delete(url)
        return response

    def send_get_request(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code {response.status_code}")

    flag = 0
    user_id = int(request.GET['user_id'])
    list_participant = json.loads(request.GET['list_participant'])
    select_task_id = request.GET['select_task_id']
    url = "http://127.0.0.1:8000/MyAPI/api/events/delete/" + select_task_id + "/"
    data_delete = send_delete_request(url)
    data_user = send_get_request("http://127.0.0.1:8000/MyAPI/api/list_user/" + str(user_id))

    if data_delete:
        print("удалено")
        flag = 1
        return render(request, 'WebManager/test4.html', {'data_user': data_user, 'flag': flag})
    else:
        print("ошибка")
        flag = 0
    return render(request, 'WebManager/test4.html', {'data_user': data_user, 'flag': flag})



