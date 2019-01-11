from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('home/delete/<list_id>', views.delete, name="delete"),

]
