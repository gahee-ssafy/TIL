
from django.contrib import admin
from django.urls import path
from articles import views

# app_name = 안해도 된다. 템플릿을 사용하지 않기 때문이다. 
 
urlpatterns = [
    path('articles/', views.article_list),
]
