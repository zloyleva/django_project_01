from django.db import models

# Create your models here.

class Product(models.Model):
	"""
	Products for uor cool store
	"""

	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.FloatField()
	image = models.CharField(max_length=255)

	def __str__(self):
		return self.name
