from django.shortcuts import render


def homepage(request):
    return render(request, 'interior/home.html')


def step2(request):
    return render(request, 'interior/step2.html')