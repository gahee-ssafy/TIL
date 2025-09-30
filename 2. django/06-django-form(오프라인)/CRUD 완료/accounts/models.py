from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# AbstractUser가 자동으로 필드생성 
class User(AbstractUser):
    pass
