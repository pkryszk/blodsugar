from django.urls import path
from .views import measurement_list,measurement_details,measurement_delete

urlpatterns = [
 path("measurement_list/", measurement_list,name="measurement_list"),
 path("measurement_details/<int:id>/", measurement_details, name="measurement_details"),
 path("measurements/<int:id>/delete/", measurement_delete, name="delete"),


]