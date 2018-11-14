from __future__ import unicode_literals
from django.db import models

class Measurement(models.Model):
    value = models.CharField(max_length=50)
    description = models.CharField( max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.value


class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.FloatField()

	def __unicode__(self):
		return self.name