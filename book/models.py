from django.db import models
from django.contrib.auth.models import AbstractUser
from category.models import Category
from django.utils import timezone
from Author.models import Authors


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250, null=True)
    password = models.CharField(max_length=250)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Books(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Authors,on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    ISBN = models.CharField(max_length=13)
    status = models.CharField(max_length=2, choices=(('1', 'Active'),('2', 'Inactive')),
    default = 1)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)
    delete_flag = models.IntegerField(default = 0)
    published_date = models.DateField()


    
class BookType(models.Model):
    name = models.CharField(max_length=250)
    

    # def __str__(self):
    #     return str(f"{self.ISBN} - {self.title} - {self.name}")

    def __str__(self):
        return self.name