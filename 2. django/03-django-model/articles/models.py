# django.db.models 모듈의 Model 부모 클래스를 상속받는다.
# django.db 내장 패키지에서 models 모듈을 임포트
from django.db import models

# Create your models here.
# Article 모델 정의(모델명 가변)
# CharField, TextField는 클래스 
#! intance(객체) 생성 시 반드시 인자값을 넣어줘야 함
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(null=True)
    # (빈출) 데이터가 처음 저장될 때만 
    created_at = models.DateTimeField(auto_now_add=True, )
    # 데이터가 저장될 때마다 갱신
    updated_at = models.DateTimeField(auto_now=True)

