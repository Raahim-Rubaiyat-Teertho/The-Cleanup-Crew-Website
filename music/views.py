from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'music/home.html')

def music(request):
    return render(request, 'music/our_music.html')

def socials(request):
    return render(request, 'music/our_socials.html')