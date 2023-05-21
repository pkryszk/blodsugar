from django.shortcuts import render, get_object_or_404, redirect
from .models import Measurement
from django.core.paginator import Paginator

ITEMS_PER_PAGE = 12

def measurement_list(request):


    page_number = request.GET.get("page", 1)
    objects_per_page = request.GET.get("per_page", ITEMS_PER_PAGE)
    measurements = Measurement.objects.all()
    p = Paginator(measurements, ITEMS_PER_PAGE)
    page_obj = p.get_page(page_number)

  #  context = {
  #      'measurements': measurements
  #  }
    return render(request, 'measurements/measurements_list.html', {"page_obj": page_obj, "per_page": objects_per_page})


def measurement_details(request, id):
    measurement = Measurement.objects.get(id=id)
    return render(request, "measurements/_measurement_details.html", {"measurement": measurement})


def measurement_delete(request, id):
    measurement = get_object_or_404(Measurement, pk=id)
    if request.method == 'POST':
        measurement_id = request.POST.get('measurement_id')
        if request.POST.get('action') == 'delete':
            Measurement.objects.get(id=id).delete()
            return measurement_list(request)
        elif request.POST.get('action') == 'back':
            return redirect("measurement_list")
    return render(request, 'measurements/measurement_delete.html', {"measurement": measurement})
