from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('delete-task/<str:name>/', views.delete, name='delete'),
    path('update/<str:name>/', views.update, name='update'),
]