from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.BookModel)
admin.site.register(models.BookCategory)
admin.site.register(models.AuthorModel)
admin.site.register(models.CustomUser)