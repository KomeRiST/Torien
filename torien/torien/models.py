from django.db import models


class BaseItem(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    image_path = models.ImageField(verbose_name='Фотография')

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Базовое свойство'
        verbose_name_plural = 'Базовые свойства'


class Size(models.Model):
    en = models.CharField(max_length=5, verbose_name='Международный')
    ru = models.PositiveSmallIntegerField(verbose_name='Российский')
    text = models.TextField(blank=True, verbose_name='Доп. данные')

    def __str__(self):
        return '{} ({}см. - {}см.)'.format(self.en, self.ru_min, self.ru_max)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    rgb16 = models.CharField(max_length=7, verbose_name='Код цвета (#000000)')
    code_color = models.CharField(max_length=10, blank=True, verbose_name='Цветовой код материала')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class KategoryThing(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    image_path = models.ImageField(upload_to='IconsThings/images', verbose_name='Иконка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категоря вещи'
        verbose_name_plural = 'Категории вещей'


class Thing(models.Model):
    mainInfo = models.OneToOneField(BaseItem, on_delete=models.CASCADE, primary_key=True, verbose_name='Инфа')
    kategory = models.ForeignKey(KategoryThing, on_delete=models.CASCADE, verbose_name='Категория')
    material = models.CharField(max_length=25, verbose_name='Материал')
    color = models.ManyToManyField(Color, verbose_name='Цвет')
    size = models.ManyToManyField(Size, verbose_name='Размер')
    cost = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.mainInfo.name

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'


class Collection(models.Model):
    mainInfo = models.OneToOneField(BaseItem, on_delete=models.CASCADE, primary_key=True, verbose_name='Инфа')
    date_start = models.DateField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.mainInfo.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'