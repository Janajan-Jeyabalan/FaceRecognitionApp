from django.shortcuts import render

def index(requeest):
    return render(request, 'index.html')