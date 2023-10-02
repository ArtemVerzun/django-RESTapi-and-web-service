## django EventAPI and dajango web_service.
### Тестовое задание от SWC на должность python backend developer
### Задание можно посмотреть по этой ссылке -> <https://drive.google.com/file/d/1LPiKXbWoZqGhX7tP-J74IzA6_jKumPSi/view>
Первая часть задания (Создать БД):
![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/652d24f9-985a-4312-bc33-73c70ee2bb59)

![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/bc7cac39-7628-4f6d-997b-c4b4bb6022a8)

Вторая часть задания (Разработать RESTful API):
* регистрация пользователя
  ![1](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/943edaea-60ce-4b46-b16c-f0fdb289de4a)
* авторизация пользователя
  была сделана примитивная авторизация путем проверки логина и пароля в таблице.
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/78e18b47-3fa2-4422-b32e-3be654efbf44)
* создание события
  ![2](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/24c03799-19ae-4fda-a8b0-e655c7d5df51)
* получение списка событий
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/4e35b1db-0b08-4e49-b149-0838c91d9d1c)
* участие в событии
  patch
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/bc3e7264-ccc5-46ec-86e0-e512654e6029)
* отмена участия в событии
  patch
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/bc3e7264-ccc5-46ec-86e0-e512654e6029)
* удаление события создателем
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/c85f19b0-76ea-4bba-b092-13610d9f76ee)
Третья часть задания (Создать простую админку):
* страница авторизации
  можно войти в свой аккаунт либо же пройти процесс регистрации
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/eb5e356b-d5a8-4f10-b3ab-a8684bee3585)
  при неправильном вводе логина и пароля появляется alert с информированием об этом
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/7b03dbe8-304b-4ffe-81c4-9d50d8b0c105)
* страница с регистрацией
  тут можно создать юзера с указанием даты и без, при ошибке регистрации появится alert
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/9dfbc8c7-1973-42a2-9228-f3eb285aaf62)
  также при успешной регистрации появится alert
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/7af6dc72-4698-4fb3-9bb9-b13aaff7b14b)
  после успешной регистрации пользователь будет перенаправлен на страницу авторизации из которой можно попасть в свой аккаунт
* страница с аккаунтом
  при открытии страницы на нее подгружаются данные пользователя и событий
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/6c6b6039-1f85-49d3-81d8-b68a4fac96f2)
  при выборе какого нибудь события оно отобразится на странице, а также его участники
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/77c16d98-c1e3-4e3d-b3a0-cb749a9ad0fb)
* про действия с событиями
  на страницу могут подгружаться три вида кнопок (Участвовать в событии, Отменить участие, Удалить событие)
  логика следующая:
  если пользователь выбирает событие, которое он не создал то он может либо участвовать в нем либо отменить участие.
  если пользователь выбирает событие, которое он создал то он может отменить участие, после чего сможет его только удалить.
  Пример:
  в аккаунте Artem Verzun выберем событие5
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/435abbf0-d725-46d2-ac5c-3e1430fd19fa)
  
  после нажатия на кнопку Artem добавляется к участникам
  ![image](https://github.com/ArtemVerzun/django-EventAPI-and-dajango-web_service/assets/143192676/85f789e6-ff44-46c5-90bd-ae7a9e5f8441)
  
  после этого можно отменить участие...
* Что еще???
  можно свободно перемещаться по веб сервису, регаться и заходить в разные аккаунты, без ошибок.
  конечно frontend не на слишком высоком уровне, и авторизацию можно сделать лучше, например токенами...
  все это поправляемо, если конечно требуется...
  тестовое задание выполнил в полном объеме, если нужны какие-нибудь доработки или объяснения жду вашего фитбека)))
  



  






