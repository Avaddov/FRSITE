from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import MediaObjectForm, GameReviewForm
from . models import MediaObject, MediaCategory, GameReview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from api_interactions import search_twitch, select_game
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')



def gallery(request):
    medias=MediaCategory.objects.all()
    return render(request, 'gallery.html', {'medias':medias})

def merch(request):
    return render(request, 'merch.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def userpage(request):
    return render(request, 'userpage.html')


@login_required
def submitmedia(request):
    if request.method == 'GET':
        return render(request, 'submitmedia.html', {'form':MediaObjectForm()})
    if request.method == 'POST':
        form=MediaObjectForm(request.POST, request.FILES)
        if form.is_valid():
            media=form.save(commit=False)
            media.author=request.user
            media.save()
            return redirect('gallery')
        return render(request, 'submitmedia.html', {'form':form})




def gamereviews(request):
    return render(request, 'gamereviews.html', {'gamereviews':GameReview.objects.all()})


def gamereview(request, id):
    return render(request, 'gamereview.html', {'GameReview':GameReview.objects.get(id=id)})    


def searchgame(request):
    games = []
    if request.method == 'POST':
        gamename=request.POST.get('gamename')
        games = search_twitch(gamename)
    return render(request, 'search_twitch.html', {'games':games})
    


def create_review(request, twitch_id):
    game=select_game(twitch_id)
    print(game)
    if request.method == 'GET':
        form=GameReviewForm()
        return render(request, 'create_review.html', {'game':game, 'form':form})
    if request.method == 'POST':
        form=GameReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.game_title=game['name']
            review.first_release_date=datetime.utcfromtimestamp(game['first_release_date'])
            # review.storyline=game['storyline']
            review.summary=game['summary']
            review.url=game['url']
            review.save()
            return redirect('gamereviews')
        return render(request, 'create_review.html', {'game':game, 'form':form})




# @login_required(redirect_field_name='login.html')
# def submit_media(request):