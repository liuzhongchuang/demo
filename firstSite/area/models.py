from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', on_delete=models.CASCADE)


class fileUpload(models.Model):
    pass