from django import forms
from logisticsSettings.models import Truck

class NameForm(forms.ModelForm):
	class Meta:
		model = Truck
		fields = ['truck_name', 'weight', 'length', 'width', 'height']
		labels = '__all__'
