from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','admin'),
        ('u','user')
    )

    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

class AuthorModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth = models.DateField(default=datetime.now)
    country = models.CharField(max_length=15,default='')

    def __str__(self):
        return f"{self.name} {self.fname}"

    class Meta:
        db_table = 'author'

class BookCategory(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)
    name = models.CharField(max_length=65,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book_category'

class BookModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=127,default='')
    category = models.ForeignKey(BookCategory,on_delete=models.SET_NULL,null=True)
    page = models.PositiveSmallIntegerField(default=1)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
