from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.


def index(request):
    # QuerySet API -> 전체데이터조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    # 단순 조회목적, GET방식이면 render
    # 생성, 수정, 삭제 POST방식이면 redirect
    return render(request, 'articles/index.html', context)

# 단일 게시글 페이지를 렌더링
def detail(request, pk):
    # QuerySet API -> 단일게시글조회 : get
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    # 게시글 생성 버튼 누를 때
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사 1. 필수 필드 값 2. 필드 조건(데이터 형식, 길이)
        if form.is_valid():
            # 저장 
            article = form.save() 
            return redirect('articles:detail', article.pk)
        
    # 게시글 생성 버튼 누르기 전이거나 다른 버튼
    else:
        form = ArticleForm() # 빈 폼
    
    # 렌더링 
    context ={
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    # 먼저 조회
    article=Article.objects.get(pk=pk)
    # 조회 후 삭제
    article.delete()
    # render? redirect? 
    # DB를 건든다. POST방식이다. redirect
    return redirect('articles:index')

# POST방식
def update(request, pk):
    # 조회 후
    article = Article.objects.get(pk = pk)
    # 수정
    if request.method == 'POST':
        # instance = article ; 작성 중인 데이터를 가져온다. 
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # instance = article ; 작성 중인 데이터를 가져온다. 
        form = ArticleForm(instance = article)
    
    # GET 방식 
    context = {
        'article' : article,
        'form' : form, # 작성 중 데이터 
    }
    return render(request, 'articles/update.html', context)