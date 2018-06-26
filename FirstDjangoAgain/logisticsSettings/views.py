from .models import Truck
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


from .forms import NameForm

def indexView(request):
	all_trucks = Truck.objects.all()
	context = {'all_trucks':all_trucks}
	return render(request, 'logisticsSettings/index.html', context)

def detailView(request, trucktype_id):
	truck_details = Truck.objects.get(id=trucktype_id)
	context = {'truck_details':truck_details}
	return render(request, 'logisticsSettings/detail.html', context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/logisticsSettings/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'logisticsSettings/create_truck.html', {'form': form})

def editView(request, trucktype_id):
    truckObject = get_object_or_404(Truck, id=trucktype_id)
    form = NameForm(instance=truckObject)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST, instance=truckObject)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/logisticsSettings/')

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'logisticsSettings/edit_truck.html', {'form': form, 'truckObject': truckObject})
