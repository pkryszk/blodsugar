import csv
import logging
import os


from django.conf import settings
from measurements.models import Measurement
import base64
import matplotlib.pyplot as plt
from io import BytesIO

LOGGER_NAME = "measurements"
LOGGER_FILENAME = "measurements_reader.log"

logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOGGER_FILENAME)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def create_measurement(row: dict):
    try:
        value, measured_date, notes = row
        m = Measurement.objects.create(value=value, measured_date=measured_date, notes=notes)
        return m
    except Exception as e:
        logger.warning(f"skipped row: {row}")
        return None


def import_measurements(filename):
    data_file_path = os.path.join(settings.BASE_DIR, 'measurements', 'data', filename)

    logger.info(f"Processing file {data_file_path}")
    with open(data_file_path, "r") as f:
        reader = csv.reader(f)
        num_of_rows = 0
        created_measurements = 0
        for row in reader:
            if create_measurement(row):
                created_measurements += 1
            num_of_rows += 1
        logger.info(f"Processed {num_of_rows} rows, created {created_measurements} measurements")




def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y):
    plt.switch_backend('AGG')
#    plt.figure(figsize(200,100))
    plt.title('')
    plt.xlabel('date')
    plt.ylabel('mg/dL')
    plt.xticks(rotation=45)
    threshold = 120
    plt.axhline(y=threshold, color='red', linestyle='--', label='high sugar')
    plt.plot(x, y,label='sugar level')
    plt.tight_layout()
    plt.legend()
    graph = get_graph()
    return graph

