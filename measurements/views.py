from django.shortcuts import render, get_object_or_404, redirect
from .models import Measurement


def measurement_list(request):
    measurements = Measurement.objects.all()
    context = {
        'measurements': measurements
    }
    return render(request, 'measurements/measurements_list.html', context)


def measurement_details(request, id):
    measurement = Measurement.objects.get(id=id)
    return render(request, "measurements/measurement_details.html", {"measurement": measurement})


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
