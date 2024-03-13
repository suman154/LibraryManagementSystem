from django.db import models

# Create your models here.
class AddBook(models.Model):
    formats = (
        ('pdf', 'PDF'),
        ('word', 'Word'),
        ('docs', 'Docs'),
        ('txt', 'Plain Text'),
        )

    file_format = models.CharField(max_length=4, choices=formats)
    book_file = models.FileField(upload_to='books/')

  
    def __str__(self):
        return str(f"{self.formats} - {self.file_format} - {self.book_file}")