from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'), 
    path('create/', views.create, name='create'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:game_id>/answer/create', views.answer_create, name='answer_create'),
]