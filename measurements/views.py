from django.shortcuts import render, get_object_or_404, redirect
from .models import Measurement
from django.core.paginator import Paginator
from measurements import utils
from django.urls import reverse

ITEMS_PER_PAGE = 12


def measurement_list(request):
    page_number = request.GET.get("page", 1)
    objects_per_page = request.GET.get("per_page", ITEMS_PER_PAGE)
    measurements = Measurement.objects.all()
    p = Paginator(measurements, ITEMS_PER_PAGE)
    page_obj = p.get_page(page_number)
    y = [measurement.value for measurement in measurements]
    x = [measurement.measured_date for measurement in measurements]
    chart = utils.get_plot(x, y)
    return render(request, 'measurements/measurements_list.html'
                  , dict(page_obj=page_obj, per_page=objects_per_page, chart=chart)

                  )


def measurement_details(request, id):
    measurement = Measurement.objects.get(id=id)
    return render(request, "measurements/_measurement_details.html", {"measurement": measurement})


def measurement_delete(request, id):
    ret_page = request.GET.get('ret_page', 1)
    measurement = get_object_or_404(Measurement, pk=id)
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            Measurement.objects.get(id=id).delete()

        objects_per_page = request.POST.get('per_page', ITEMS_PER_PAGE)
        redirect_url = f"{reverse('measurement_list')}?page={ret_page}&per_page={objects_per_page}"
        return redirect(redirect_url)

    return render(request, 'measurements/measurement_delete.html', {"measurement": measurement, "ret_page": ret_page})
