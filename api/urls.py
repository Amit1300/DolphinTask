
from django.urls import path
from .views import UserApi
urlpatterns = [
    path('api/',UserApi.as_view()),
    path('api/<int:pk>',UserApi.as_view())
]
