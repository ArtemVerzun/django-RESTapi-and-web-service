## django EventAPI and dajango web_service.
### Тестовое задание от SWC на должность python backend developer
### Задание можно посмотреть по этой ссылке -> <https://drive.google.com/file/d/1LPiKXbWoZqGhX7tP-J74IzA6_jKumPSi/view>
Первая часть задания (Создать БД):
![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/652d24f9-985a-4312-bc33-73c70ee2bb59)

![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/bc7cac39-7628-4f6d-997b-c4b4bb6022a8)

Вторая часть задания (Разработать RESTful API):
* регистрация пользователя
  
  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/75033af0-8417-4b36-8f04-e2035f1cad44)
  
* авторизация пользователя
  была сделана примитивная авторизация путем проверки логина и пароля в таблице.
  
  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/5d7d554c-f3dc-480b-bc5f-e5a31c78a537)

* создание события
  
  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/154f4754-0d5d-4af1-8b90-69a22855356a)
  
* получение списка событий
  
  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/834b92b4-b9f7-4f34-8c2f-216db18571de)

* участие в событии
  patch

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/6ecf066a-0b50-4f4d-80a1-da83bda14295)

* отмена участия в событии
  patch

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/c32d6df0-d281-4141-b94f-b1eeb55ba96d)

* удаление события создателем

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/01b8027a-17c6-4a29-a142-56437d5a691b)

Третья часть задания (Создать простую админку):
* страница авторизации
  можно войти в свой аккаунт либо же пройти процесс регистрации

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/ab195d29-8e01-4302-b1ff-15cdaaa2a4c7)

  при неправильном вводе логина и пароля появляется alert с информированием об этом

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/56c700e0-11fa-41cb-91e1-a7cc281e6e85)

* страница с регистрацией
  тут можно создать юзера с указанием даты и без, при ошибке регистрации появится alert
  
  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/02ec7f17-1355-4a46-8a8c-16de5c1da606)

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/ecd88cd8-8403-4408-a55d-9b7f4a517588)

  после успешной регистрации пользователь будет перенаправлен на страницу авторизации из которой можно попасть в свой аккаунт
  
* страница с аккаунтом
  при открытии страницы на нее подгружаются данные пользователя и событий

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/cd04723c-bc69-4fc4-a925-750fbc1a5215)

  при выборе какого нибудь события оно отобразится на странице, а также его участники

  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/19d8d8ec-d394-4b8f-ab4d-3d02e8a16681)

* про действия с событиями
  на страницу могут подгружаться три вида кнопок (Участвовать в событии, Отменить участие, Удалить событие)
  логика следующая:
  если пользователь выбирает событие, которое он не создал то он может либо участвовать в нем либо отменить участие.
  если пользователь выбирает событие, которое он создал то он может отменить участие, после чего сможет его только удалить.
  Пример:
  в аккаунте Artem Verzun выберем событие5
  
  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/0c98891a-d5f4-4596-bf90-0231fb7254a6)
  
  после нажатия на кнопку Artem добавляется к участникам
  ![image](https://github.com/ArtemVerzun/django-RESTapi-and-web-service/assets/143192676/734eddf6-f500-4644-a995-589223d137d1)

  после этого можно отменить участие...
  
* Что еще???
  можно свободно перемещаться по веб сервису, регаться и заходить в разные аккаунты, без ошибок.
  конечно frontend не на слишком высоком уровне, и авторизацию можно сделать лучше, например токенами...
  все это поправляемо, если конечно требуется...
  тестовое задание выполнил в полном объеме, если нужны какие-нибудь доработки или объяснения жду вашего фитбека)))
  



  






