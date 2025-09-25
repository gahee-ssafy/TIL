
from django.contrib import admin
from django.urls import path
from . import views

# url naming pattern 때문에 app_name을 작성 
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # pk의 변수에 할당된 값은 views.py의 detail 함수 pk 매개변수로 
    path('<int:pk>/', views.detail, name='detail'),
]
