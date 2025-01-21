from django.urls import path
from todoapp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete-task/<str:name>/', views.delete, name='delete'),
    path('update/<str:name>/', views.update, name='update'),
]