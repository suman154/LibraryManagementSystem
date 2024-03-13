from django.contrib import admin
from .models import Books,BookType,User

# Register your models here.
admin.site.register(Books)
admin.site.register(BookType)
admin.site.register(User)