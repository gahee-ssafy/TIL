from django.contrib import admin
from django.urls import path

from . import views

# URL 네임스페이스 : 다른앱과 혼동하지 않기 위해
# {% url 'articles:index' %} -> named URL pattern
app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('dinner/', views.dinner, name = 'dinner'),
    path('search/', views.search, name = 'search'),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
    # variable routing
    path('<int:number>/', views.detail, name='detail'),
]
