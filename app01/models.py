from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Userinfo(AbstractUser):
    username = models.CharField(verbose_name='用户名',max_length=32,unique=True)
    password = models.CharField(verbose_name='密码',max_length=128)
    mobile_phone = models.CharField(verbose_name='手机号',max_length=11)

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name