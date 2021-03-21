from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')



def gallery(request):
    return render(request, 'gallery.html')

def merch(request):
    return render(request, 'merch.html')

def userpage(request):
    return render(request, 'userpage.html')