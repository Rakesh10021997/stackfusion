from django.db import models

# Create your models here.
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.

name = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed.')
number = RegexValidator(r'^[0-9]{10}$', 'Only digits are allowed.')





class Register(models.Model):
    first_name =models.CharField(max_length=20, null=True,default=" ",validators=[name])
    dob=models.DateField()
    email=models.EmailField(max_length=100,null=True,default=" ")
    mobilenumber=models.CharField(max_length=10,null=True,validators=[number])


# class Register(models.Model):
#     first_name =models.CharField(max_length=30,null=True,default="",validators=[name])
#     dob =models.DateField()
#     email =models.EmailField(max_length=30,null=True,default='')
# 	mobilenumber =models.CharField(max_length=10,null=True)
#     def __str__(self):
#         return self.first_name
