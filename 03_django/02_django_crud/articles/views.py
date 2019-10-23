from IPython import embed
# embed : 서버 잠깐 멈추게하는 것
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article, Comment

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
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.save()
        # embed()
        return redirect(article)
    # NEW
    else:
        return render(request, 'articles/create.html')


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    # article.get_absolute_url()
    context = {'article': article, 'comments': comments,}
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)


def comments_create(request, article_pk):
    # 댓글을 달 게시글이 필요
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # form에서 넘어온 댓글 정보 받아오기
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect(article)
        # 다른 방식 (get_absolute_url을 구현하지 못했을 경우)
        # return redirect('articles:detail' article.pk)
        # return redirect('articles:detail' article_pk)
    else:
        return redirect(article)


def comments_delete(request, comment_pk, article_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('articles:detail', article_pk)

'''
def comments_delete(request, comment_pk, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect(article)
'''
