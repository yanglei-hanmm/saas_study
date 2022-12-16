from django.urls import path

from app01 import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('sms/', views.SmsView.as_view()),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('image_code/',views.ImageCodeView.as_view(),name='image_code'),


]