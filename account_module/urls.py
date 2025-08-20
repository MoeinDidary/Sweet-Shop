from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterFormView.as_view(), name='register_view'),
    path('login', views.LoginFormView.as_view(), name='login_view'),
    path('logout', views.LogoutView.as_view(), name='logout_view')
]
