from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import MediaObjectForm
from . models import MediaObject, MediaCategory, GameReview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')



def gallery(request):
    medias=MediaCategory.objects.all()
    return render(request, 'gallery.html', {'medias':medias})

def merch(request):
    return render(request, 'merch.html')

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



# @login_required(redirect_field_name='login.html')
# def submit_media(request):