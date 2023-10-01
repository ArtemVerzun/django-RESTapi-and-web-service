from django.urls import path
from .views import UserRegisterView, UserLoginView, EventCreateView, EventListView, EventCancelParticipationView, EventDeleteView, AddRecordView, ListUserInfo, FindCreator, ListUserInfo2

urlpatterns = [
    path('api/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/add/<int:pk>/', AddRecordView.as_view()),
    path('api/find/<str:creator>/', FindCreator.as_view()),
    path('api/list_user/<int:pk>/', ListUserInfo.as_view()),
    path('api/list_user/<str:login>/', ListUserInfo2.as_view()),
    path('api/login/<str:login>/<str:password>/', UserLoginView.as_view()),
    path('api/events/create/', EventCreateView.as_view(), name='event-create'),
    path('api/events/', EventListView.as_view(), name='event-list'),
    path('api/events/cancel-participation/<int:pk>/', EventCancelParticipationView.as_view(), name='event-cancel-participation'),
    path('api/events/delete/<int:pk>/', EventDeleteView().as_view(), name='event-delete'),
]
