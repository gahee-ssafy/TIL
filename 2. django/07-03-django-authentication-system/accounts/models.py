from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

# admin 계정의 비밀번호는 "qwer1234!"