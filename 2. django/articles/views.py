from django.shortcuts import render
from articles import views

# Create your views here.
def index(request):
    # index.html 파일 페이지를 render 해라
    return render(request, 'articles/index.html')
