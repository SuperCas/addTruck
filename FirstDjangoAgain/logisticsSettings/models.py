from django.db import models

class Truck(models.Model):
	truck_name = models.CharField(max_length=100)

	def __str__(self):
		return self.truck_name

class Dimension(models.Model):
	trucktype = models.ForeignKey('Truck', on_delete=models.CASCADE, related_name='dimensions')
	weight = models.CharField(max_length=100)
	length = models.CharField(max_length=100)
	width = models.CharField(max_length=100)
	height = models.CharField(max_length=100)


	def __str__(self):
		return self.weight