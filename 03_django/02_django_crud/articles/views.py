from IPython import embed
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


def new(request):
    return render(request, 'articles/new.html')


# 직접적으로 모델에 저장하는 역할
def create(request):
    # 서버를 일시정지 시켜주는 역할
    # embed()
    # 검증 단계 추가
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        # 데이터를 저장하는 첫 번째 방법
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()

        # 두 번째 방법
        article = Article(title=title, content=content)
        # 검증 연결
        article.full_clean()
    except ValidationError:
        raise ValidationError('Error')
    # 아무 오류가 발생하지 않았을 때
    else:
        article.save()
        # 세 번째 방법
        # Article.objects.create(title=title, content=content)
        return redirect(f'/articles/{article.pk}') # 메인페이지 (index값으로 전환)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}')