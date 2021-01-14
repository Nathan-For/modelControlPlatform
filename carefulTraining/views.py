from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def carefulTraining(request):
    return render(request, 'carefulTraining.html')
