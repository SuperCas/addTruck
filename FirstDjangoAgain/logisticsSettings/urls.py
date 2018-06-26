from django.urls import path, re_path
from . import views

app_name = 'logisticsSettings'

urlpatterns = [
	# /logisticsSettings/
	re_path(r'^$', views.indexView, name='indexView'),

	# /logisticsSettings/<trucktype_id>/
	re_path(r'^(?P<trucktype_id>\d+)/$', views.detailView, name='detailView'),

	# /logisticsSettings/addTruck
	re_path(r'^addTruck$', views.get_name, name='get_name'),

	# /logisticsSettings/editTruck
	re_path(r'^editTruck/(?P<trucktype_id>\d+)/$', views.editView, name='editView'),
]