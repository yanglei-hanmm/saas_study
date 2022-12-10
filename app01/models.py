from django.db import models

# Create your models here.

class Userinfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32,unique=True)
    password = models.CharField(verbose_name='密码',max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号',max_length=11)

