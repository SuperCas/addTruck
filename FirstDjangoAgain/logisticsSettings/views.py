from .models import Truck
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .forms import TruckForm

def indexView(request):
	all_trucks = Truck.objects.all()
	context = {'all_trucks':all_trucks}
	return render(request, 'logisticsSettings/index.html', context)

def detailView(request, trucktype_id):
	truck_details = Truck.objects.get(id=trucktype_id)
	context = {'truck_details':truck_details}
	return render(request, 'logisticsSettings/detail.html', context)


def createView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TruckForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('logisticsSettings:indexView'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TruckForm()

    return render(request, 'logisticsSettings/create_truck.html', {'form': form})

def editView(request, trucktype_id):
    truckObject = get_object_or_404(Truck, id=trucktype_id)
    form = TruckForm(instance=truckObject)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TruckForm(request.POST, instance=truckObject)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('logisticsSettings:indexView'))

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'logisticsSettings/edit_truck.html', {'form': form, 'truckObject': truckObject})


def deleteView(request, trucktype_id):
    truckObject = get_object_or_404(Truck, id=trucktype_id)
    form = TruckForm(instance=truckObject)

    if request.method == 'POST':
        form = TruckForm(request.POST, instance=truckObject)
        truckObject.delete()

        return HttpResponseRedirect(reverse('logisticsSettings:indexView'))

    else:
        form = TruckForm(instance=truckObject)

    return render(request, 'logisticsSettings/delete_truck.html', {'form': form, 'truckObject': truckObject})
