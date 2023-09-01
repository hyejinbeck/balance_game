from django.db import models

# Create your models here.

class Game(models.Model): 
    title = models.CharField(max_length=50) #제목
    question = models.TextField()   # 질문
    answer1 = models.TextField()
    answer2 = models.TextField()

class Answer(models.Model): 
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    choice = models.TextField()
    