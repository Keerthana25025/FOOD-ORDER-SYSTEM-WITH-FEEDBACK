from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30)
	rollnumber=models.CharField(max_length=30)
	age=models.IntegerField()
	mobile=models.CharField(max_length=10)
	email=models.EmailField(max_length=30)
	address=models.CharField(max_length=30)

	def __str__(self):
		return self.name+" "+self.email


class Registers(models.Model):
	genders=[('Male','Male'),('Female','Female')]
	branches=[('CSE','CSE'),('ECE','ECE'),('IT','IT'),('EEE','EEE')]

	name=models.CharField(max_length=30)
	mobile=models.CharField(max_length=10)
	age=models.IntegerField()
	gender=models.CharField(max_length=10,choices=genders,null=True)
	branch=models.CharField(max_length=10,choices=branches,null=True)


class Profile(models.Model):
	name=models.CharField(max_length=30)
	image=models.ImageField(upload_to="Profiles/")