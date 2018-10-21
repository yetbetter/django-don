from django.urls import path

from profiles import views

urlpatterns = [
    path('balance', views.get_user_balance, name='profile-balance')
]