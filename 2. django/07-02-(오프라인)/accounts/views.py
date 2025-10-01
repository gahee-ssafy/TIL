from django.shortcuts import render,redirect

# auth는 Model Form을 안쓴다.
# built-in form 을 쓴다.
from django.contrib.auth.forms import (
    AuthenticationForm # 로그인을 위한 폼
)

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    # 로그인 버튼을 눌렀을 때 (POST)
    if request.method == 'POST':
        # request.POST : 사용자가 입력한 ID, PASSWORD
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효성 검사 성공시 로그인 처리
            # get_user() : 인증된 사용자의 객체, 로그인 정보 검토 완 
            auth_login(request, form.get_user())
            return redirect('articles:index')
        
    else: 
        form = AuthenticationForm() # ID, PASSWORD가 빈 폼

    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html', context)

from django.contrib.auth.decorators import login_required

# 로그인 상태만 로그아웃
@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


from .forms import CustomUserCreationForm

def signup(request):
    # 기가입자 vs 미가입자로 나뉜다. 
    if request.user.is_authenticated: 
        return redirect('articles:index') # 기가입자면, 홈페이지로. 
    
    if request.method == 'POST': # 가입 버튼!을 눌렀을 때
        form =CustomUserCreationForm(request.POST)
        if form.is_valid(): # 1. 유효성 검사 
            user = form.save() # 2. DB 저장 
            auth_login(request, user) # 3. 로그인
            return redirect('articles:index') # 홈페이지로 
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form, #폼 넘겨서 html에 쓸려고 
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # request.user : 현재 로그인 되어있는 user. 
    request.user.delete()
    return redirect('articles:index') # 홈페이지로 