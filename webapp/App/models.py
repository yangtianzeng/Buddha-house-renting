from datetime import datetime

from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64)
    icon = models.ImageField(upload_to="iocns")
    sex = models.BooleanField(default=False)

class CityModel(models.Model):
    citys = models.CharField(max_length=32)

class RegionModel(models.Model):
    city = models.ForeignKey("CityModel")
    regions = models.CharField(max_length=32)

class HouseModel(models.Model):
    region = models.ForeignKey("RegionModel")
    title = models.CharField(max_length=500)  # 名字
    price = models.CharField(max_length=64)
    paytype = models.CharField(max_length=64)
    renttype = models.CharField(max_length=64)
    hometype = models.CharField(max_length=64)
    area = models.CharField(max_length=64)
    decorade = models.CharField(max_length=64)
    address = models.CharField(max_length=500)
    linkman = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    img = models.CharField(max_length=500)
    features = models.CharField(max_length=2000)

class LikeModel(models.Model):
    user = models.ForeignKey("UserModel")
    house = models.ForeignKey("HouseModel")

class BlogModel(models.Model):
    user = models.ForeignKey("UserModel")
    rid = models.IntegerField(default=0)
    content = models.CharField(max_length=5000)
    time = models.DateTimeField(default=datetime.utcnow)
    city = models.ForeignKey("CityModel")

