from django.db import models

# Create your models here.


class NewsInfo(models.Model):
    goodsName = models.CharField(max_length=30)  # 商品名称
    goodsUrl = models.CharField(max_length=60)  # 商品链接
    goodsId = models.CharField(max_length=20)  # 商品ID
    # goodsClassify = Field()  # 商品分类
    goodsPrice = models.CharField(max_length=30)  # 商品价格
    goodsCommentCount = models.CharField(max_length=10)  # 评论总数
    hp = models.CharField(max_length=10)  # 好评
    zp = models.CharField(max_length=10)  # 中评
    cp = models.CharField(max_length=10)  # 差评