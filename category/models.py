from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250, blank=True, null=True)
    ststus = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')),
    default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(f"{self.name}")

