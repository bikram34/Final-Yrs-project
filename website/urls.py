
from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name="home"),
  path('register/', views.register, name="register"),
  path('edit/', views.edit, name="edit"),
  path('prediction/', views.prediction, name="prediction"),
  path('result', views.result, name="result"),
  path('user_result', views.user_result, name="user_result"),
  path('login/', views.login, name="login"),
  path('doctors/', views.doctors, name="doctors"),
  path('update/', views.update, name="update"),
  path('about/', views.about, name="about"),
  path('signup', views.signup, name="signup"),
  path('user_login', views.user_login, name="user_login"),
  path('user_logout', views.user_logout, name="user_logout"),
]
