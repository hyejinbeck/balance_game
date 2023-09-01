from django import forms
from .models import Game, Answer

class GameForm(forms.ModelForm): 
        # 일단 여기 빈공간 
    class Meta:    # 비표기 데이터 
        model = Game 
        fields = '__all__'

class AnswerForm(forms.ModelForm):
    class Meta: 
        model = Answer
        #fields = '__all__'
        #fields = ('choice',) 
        exclude = ('game',)

        