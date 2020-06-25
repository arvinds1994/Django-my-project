from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Teacher(models.Model):
    pass


class Student(models.Model):
    faculty_name = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=20)
    surname= models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    standerd = models.CharField(max_length=20)
    create_date = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.create_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("student_detail",kwargs={'pk':self.pk})

    def __str__(self):  
        return self.first_name

