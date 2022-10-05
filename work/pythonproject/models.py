from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    telphone = models.CharField(max_length=255)
    def __str__(self):
        return self.name, self.telphone



class Registration(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Addition(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    detai = models.CharField(max_length=255)