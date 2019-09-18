from IPython import embed
# embed : 서버 잠깐 멈추게하는 것
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# READ 해오기 위한 작업
def index(request):
    # 역순으로 받으려면 .order_by('-')
    articles = Article.objects.all().order_by('-pk') # DB가 변경
    # articles = Article.objects.all()[::-1] # python이 변경
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


# 직접적으로 모델에 저장하는 역할
def create(request):
    # CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content') 
        article = Article(title=title, content=content)
        article.save()
        return redirect(article)
    # NEW
    else:
        return render(request, 'articles/create.html')


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # article.get_absolute_url()
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)

