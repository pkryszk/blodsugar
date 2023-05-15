from django.core.management.base import BaseCommand
import os,sys
from measurements.utils import import_measurements


class Command(BaseCommand):
    help = "reads blodsugar measuerements from a given file"

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str, help="csv file")

    def handle(self, *args, **options):
        filename = options["filename"]
        import_measurements(filename)
       # print(f"Blod sugar measurements from file {filename} inserted into database")