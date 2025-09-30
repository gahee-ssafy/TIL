from django.contrib import admin
# 추가 
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# User와 UserAdmin 모델을 등록
admin.site.register(User, UserAdmin)
