from django.shortcuts import render, redirect

# Create your views here.
from .admin import Article

def index(request):
    # 전체 데이터 조회
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    # 단순조회, GET 방식: render
    # 생성, 수정, 삭제, POST 방식: redirect 
    # index.html로 연결된다. 
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

