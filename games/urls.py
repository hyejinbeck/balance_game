from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),  # 메인 
    path('create/', views.create, name='create'), # 게임생성 
    path('<int:id>/', views.detail, name='detail'), # 게임 하나하나 

    path('<int:game_id>/answer/create', views.answer_create, name='answer_create'),
    # 
    path('<int:game_id>/<int:user_choice>',views.choice,name='choice'),
]