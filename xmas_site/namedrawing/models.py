from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# for updating models, delete the db
# go to project/app/migrations folder
# delete everything except the init.py file (including dir)
# python manage.py migrate --run-syncdb
# run makemigrations and migrate
# https://stackoverflow.com/questions/26927705/django-migration-error-you-cannot-alter-to-or-from-m2m-fields-or-add-or-remove/39223849

#should be able to delete Person
class Person(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length = 50)
	members = models.ManyToManyField(User, through='Membership')
	def __str__(self):
		return self.name
		
# https://docs.djangoproject.com/en/2.0/topics/db/models/
class Membership(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	date_joined = models.DateField(default=datetime.date.today)
	isAdmin = models.BooleanField(default=False)
