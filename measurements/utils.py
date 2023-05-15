import csv,os,logging
from measurements.models import Measurement
from django.conf import settings
LOGGER_NAME = "measurements"
LOGGER_FILENAME ="measurements_reader.log"

logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOGGER_FILENAME)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def create_measurement(row: dict):
    try:
        value,measured_date,notes = row
        m = Measurement.objects.create( value=value,measured_date=measured_date,notes=notes)
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
