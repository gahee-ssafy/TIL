from django.shortcuts import render
# AuthenticationForm: 로그인을 위한 폼 
from django.contrib.auth.forms import AuthenticationForm
# 함수명 중복으로 별명 설정; as auth_login
from django.contrib.auth import login as auth_login
# Create your views here.

def login(request):
    pass
  