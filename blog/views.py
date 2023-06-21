from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ola(request):
    return HttpResponse('Olá, Django')