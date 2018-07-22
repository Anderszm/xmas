from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 50)

class Group(models.Model):
	groupname = models.CharField(max_length = 50)
	people = models.ManyToManyField(Person)
	