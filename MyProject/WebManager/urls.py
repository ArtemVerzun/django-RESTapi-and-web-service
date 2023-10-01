from django.urls import path
from .views import index, account, select_task, add_participant, del_participant, no_participant, registration, registration_form

urlpatterns = [
    path('', index, name='index'),
    path('account', account, name='account'),
    path('account/<str:login>/<str:x>/', select_task, name='select_task'),
    path('registration_form/', registration_form, name='registration_form'),
    path('registration/', registration, name='registration'),
    path('add/participant/', add_participant, name='add_participant'),
    path('del/participant/', del_participant, name='del_participant'),
    path('no/participant/', no_participant, name='no_participant'),
]
