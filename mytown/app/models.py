from django.db import models

class Contact(models.Model):
    name=models.TextField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField(max_length=200)
    def __str__(self):
        return self.name
