from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    GENDER = (
        ("M","남자"),
        ("F","여자"),
    )
    birthday = models.DateField(blank=True, null=True)#둘다 true인 경우-로그인에 상관이없는 경우
    gender = models.CharField(max_length=2, blank=True, null=True, choices=GENDER)