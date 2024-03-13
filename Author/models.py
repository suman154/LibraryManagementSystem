from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=250)
    bio = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.name
    