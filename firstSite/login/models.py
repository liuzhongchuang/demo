from django.db import models

# Create your models here.

"""
下面的类必须要继承models.Model。
"""
class UserInfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
