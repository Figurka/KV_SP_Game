from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)