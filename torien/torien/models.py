from django.db import models


class BaseItem(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    image_path = models.ImageField()

    def __str__(self):
        return self.name


class Size(models.Model):
    en = models.CharField(max_length=5)
    ru_min = models.PositiveSmallIntegerField()
    ru_max = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True)

    def __str__(self):
        return '{} ({}см. - {}см.)'.format(self.en, self.ru_min, self.ru_max)


class Color(models.Model):
    name = models.CharField(max_length=20)
    rgb16 = models.CharField(max_length=7)
    code_color = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class KategoryThing(models.Model):
    name = models.CharField(max_length=25)
    image_path = models.ImageField(upload_to='IconsThings/images')

    def __str__(self):
        return self.name


class Thing(models.Model):
    kategory = models.ForeignKey(KategoryThing, on_delete=models.CASCADE)
    mainInfo = models.OneToOneField(BaseItem, on_delete=models.CASCADE, primary_key=True)
    size = models.ManyToManyField(Size)
    cost = models.PositiveIntegerField()
    material = models.CharField(max_length=25)
    color = models.ManyToManyField(Color)

    def __str__(self):
        return self.mainInfo.name


class Collection(models.Model):
    mainInfo = models.OneToOneField(BaseItem, on_delete=models.CASCADE, primary_key=True)
    date_start = models.DateField(auto_now=True)

    def __str__(self):
        return self.mainInfo.name
