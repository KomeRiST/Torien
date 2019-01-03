from django.contrib import admin
from . import models

admin.site.register(models.Collection)
admin.site.register(models.BaseItem)
admin.site.register(models.Color)
admin.site.register(models.Size)
admin.site.register(models.Thing)
admin.site.register(models.KategoryThing)
