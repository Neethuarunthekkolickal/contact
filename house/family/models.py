from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=500)
    phone=models.TextField(max_length=12)
    def __str__(self):
        return self.name
class Fees(models.Model):
    amount=models.IntegerField(max_length=10)
    date=models.DateField(max_length=10)
    balance=models.IntegerField(max_length=10)
    def __str__(self):
        return str(self.amount)
class Mark(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    malayalam=models.IntegerField(max_length=3)
    english=models.IntegerField(max_length=3)
    science=models.IntegerField(max_length=3)
    def __str__(self):
        return str(self.malayalam)


