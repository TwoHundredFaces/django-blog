from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse
from blog.models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

def ola(request):
    #return HttpResponse('Olá, Django')
    return render(request, 'home.html')
    posts = Post.objects.all()
    context = {'posts_list': posts }
    return render(request, 'posts.html', context) 