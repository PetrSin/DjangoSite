from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    titles={
        'title': 'Главная страница',
        'values': ['Hello', 'Some', 123],
        'user': {
            'name': 'Rob',
            'age': 23,
            'hobbi': 'Football'
        }
    }
    return render(request, 'main/index.html', titles)

def second(request):
    return render(request, 'main/about.html')
