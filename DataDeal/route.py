from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse


# Create your views here.

def GetTest(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def GetTestasd(request):
    return JsonResponse({'b': '123'})


def Show(request):
    return render(request, 'First.html')


def Jinlu(request):
    return render(request, 'jinlu.html')

def find(request):
    return render(request, 'find.html')

def a(request):
    content = {
        "衬衫": 5,
        "羊毛衫": 20, "雪纺衫": 36, "裤子": 10, "高跟鞋": 10, "袜子": 20
    }
    return JsonResponse(content)
