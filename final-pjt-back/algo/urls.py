from django.urls import path
from . import views

app_name = 'algo'
urlpatterns = [
    path('moviecup/', views.moviecup_list, name='moviecup_list'),
    path('moviecup/winner/', views.winner, name='winner'),
    path('lottery/', views.lottery, name='lottery')
]