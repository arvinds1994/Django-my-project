from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Teacher(models.Model):
    pass


class Student(models.Model):
    name = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=20)
    surname= models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    standerd = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse("home",kwargs={'pk':self.pk})

    def __str__(self):  
        return self.name

