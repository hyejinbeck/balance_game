from django.shortcuts import render, redirect
from .models import Game, Answer
from .forms import GameForm, AnswerForm

# Create your views here.
def index(request): 
    games = Game.objects.all()

    context = {
        'games' : games , 
    }

    return render(request, 'index.html', context)


def create(request): 
    if request.method == 'POST': # post요청일때 
        form = GameForm(request.POST)   # 프론트엔드에 검증
        if form.is_valid():           #통과되면 백엔드에 재검증
            form.save()            # 다 통과된것만 저장 

            return redirect('games:index')      
    else:                        # get요청일때  
        form = GameForm()

    context = {
        'form': form,
    } 
    return render(request,'form.html', context)

def detail(request,id):
    game = Game.objects.get(id=id)
    answer_form = AnswerForm()

    context = {
        'game': game, 
        'answer_form': answer_form,
    }
    
    return render(request, 'detail.html', context)

def answer_create(request, game_id): 

    # 사용자가 입력한 정보를 form에 입력
    answer_form = AnswerForm(request.POST)  

    # 유효성 검사 (프론트엔드)
    if answer_form.is_valid():  
        # form을 저장(백엔드)-> 추가로 넣어야 하는 데이터를 넣기 위해, 저장 멈춰!
        answer = answer_form.save(commit=False)
        # 어떤 데이터가 필요하다? 그럼 잠깐 저장 멈춰 
        
        game = Game.objects.get(id=game_id)

        answer.game = game 

        answer.save()

        return redirect('games:detail', id=game_id)

