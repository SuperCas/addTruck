from django.db import models

class Truck(models.Model):
	truck_name = models.CharField(max_length=100)
	weight = models.CharField(max_length=100, null = True, blank = True)
	length = models.CharField(max_length=100, null = True, blank = True)
	width = models.CharField(max_length=100, null = True, blank = True)
	height = models.CharField(max_length=100, null = True, blank = True)

	def __str__(self):
		return self.truck_name
