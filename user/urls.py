from django.urls import path
from .views import  UserRegister, UserLogin

urlpatterns = [
    path('add_user', UserRegister.as_view(),
        name='add_user'),
    path('login', UserLogin.as_view(),name='login'),    
]