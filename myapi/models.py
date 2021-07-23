from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=60)
	password = models.CharField(max_length=60)

	def __str__(self):
		return self.username


class Ingredient(models.Model):
	name = models.CharField(max_length=60)
	aisle = models.CharField(max_length=60)
	shelf = models.CharField(max_length=60)
	column = models.CharField(max_length=60)
	row = models.CharField(max_length=60)

	def __str__(self):
		return self.name
		
class Medication(models.Model):
	name = models.CharField(max_length=60)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient)

	def __str__(self):
		return self.name