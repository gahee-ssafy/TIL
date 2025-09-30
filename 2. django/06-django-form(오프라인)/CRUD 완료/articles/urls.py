from django.contrib import admin
from django.urls import path
from . import views

# url naming pattern
app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    # variable routing
    # pk의 변수에 할당된 값은 views.py의 detail함수의 pk 매개변수로
    path('<int:pk>/', views.detail, name = 'detail'),
    # 게시글 생성 페이지를 단순히 렌더링 하는 역할
    # path('new/', views.new, name = 'new'),
    # 렌더링 + 리다이렉트 
    path('create/', views.create, name = 'create'),
    # 단일 게시글 조회 후 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 페이지 렌더링 (단일 게시글 조회 먼저)
    # path('<int:pk>/edit/', views.edit, name = 'edit'),
    # 페이지 리다이렉트
    path('<int:pk>/update/', views.update, name = "update"),

]