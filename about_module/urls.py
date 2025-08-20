from django.urls import path
from . import views

urlpatterns = [
    path('about-us', views.AboutView.as_view(), name='about_view')
]
