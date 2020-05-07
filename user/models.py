from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Register(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length = 100)
#     username = models.CharField(max_length = 100)
#     password = models.CharField(max_length = 100)
#     confirm = models.CharField(max_length = 100)

    # def __str__(self):
    #     self.last_name

class Create(models.Model):
    title = models.CharField(max_length=100)

class Assignment(models.Model):


    ques = models.TextField()
    # user = models.OneToOneField(User, on_delete = models.CASCADE)

    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    # userid = models.IntegerField()

    # uid = User.id
    # id = User.id
    def __str__(self):
        return self.ques

 