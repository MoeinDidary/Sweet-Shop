from django.urls import path
from . import views

urlpatterns = [
    path('user-panel', views.EditUserProfilePageView.as_view(), name='user_panel_view')
]
