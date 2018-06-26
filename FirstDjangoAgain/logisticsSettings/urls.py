from django.urls import path, re_path
from . import views

app_name = 'logisticsSettings'

urlpatterns = [
	# /l/
	re_path(r'^$', views.indexView, name='indexView'),

	# /music/<album_id>/
	re_path(r'^(?P<trucktype_id>\d+)/$', views.detailView, name='detailView'),

] 