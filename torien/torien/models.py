from django.db import models


class BaseItem(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    image_path = models.FilePathField(path="/home/images")


class Size(models.Model):
    en = models.CharField(max_length=5)
    ru_min = models.PositiveSmallIntegerField()
    ru_max = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True)


class Color(models.Model):
    name = models.CharField(max_length=20)
    rgb16 = models.CharField(max_length=7, min_length=7)
    code_color = models.CharField(max_length=10, blank=True)


class Thing(models.Model):
    mainInfo = models.OneToOneField(BaseItem, on_delete=models.CASCADE, primary_key=True)
    size = models.ManyToManyField(Size)
    cost = models.PositiveIntegerField()
    material = models.CharField(max_length=25)
    color = models.ManyToManyField(Color)


class Collection(models.Model):
    mainInfo = models.OneToOneField(BaseItem, on_delete=models.CASCADE, primary_key=True)
    date_start = models.DateField(auto_now=True)
