from django.contrib import admin

# Register your models here.
from .models import Article

# admin.site 에 Article 모델을 등록한다.
admin.site.register(Article)