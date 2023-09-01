from django.shortcuts import render, redirect
from .models import Game, Answer
from .forms import GameForm, AnswerForm

# Create your views here.

# 메인화면 보여주는기능
def index(request):   
    games = Game.objects.all()

    context = {
        'games' : games , 
    }

    return render(request, 'index.html', context)

# 게임생성 기능
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

# 게임 하나하나 개별페이지
def detail(request,id):
    # Game클래스 그 자체(제목,질문)
    game = Game.objects.get(id=id)
    # Answer 선택할수 있게 
    answer_form = AnswerForm()

    context = {
        'game': game, 
        'answer_form': answer_form,
    }
    
    return render(request, 'detail.html', context)

def answer_create(request, game_id): 

    # 사용자가 정답 클릭한거(제출한거 POST로 받아서 씌움)
    answer_form = AnswerForm(request.POST)  

    # db에 선택지 보낸야함 
    if answer_form.is_valid():  

        answer = answer_form.save(commit=False)
        # class AnswerForm에서 뺀거 있으니까 멈춰 
        # 뺀거 game 선택지, 어떤거하나하나니까 games 말고 game
        game = Game.objects.get(id=game_id)

        # 정답지(클릭한거) db 보내기전에 합치기
        answer.game = game 
        # 클릭한거 뭔지 저장 
        answer.save()
        #클릭한상태에서 그대로 
        return redirect('games:detail', id=game_id)

# 클릭한거 받아서 어떤거 클릭했는지 구현 
def choice(request, game_id, user_choice):
    game = Game.objects.get(id=game_id)

    # 뭘 눌렀는지에 따라 값 달라짐 
    if user_choice == 1:
        choice_answer = game.answer1
    elif user_choice == 2:
        choice_answer = game.answer2
    else:
        chosen_answer = "Invalid Choice"  # 예외 처리 

    context = {
        'game': game,
        'choice_answer': choice_answer,
    }

    return render(request, 'choice.html', context)