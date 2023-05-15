#from measurements.models import Measurement
#import faker
from datetime import datetime, timedelta
import random,csv
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

current_date = start_date

n = 65
m = 120
x = 10
reasons =['Medications','Stress','Illness or infection','Overuse of Alcohol']

next_number=70
with open('data/data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    while current_date <= end_date:
        date_string = current_date.strftime("%Y-%m-%d")
        next_number = random.randint(max(n, next_number - x), min(m, next_number + x))
        reason=''
        if next_number>100:
            reason=random.choice(reasons)
        current_date += timedelta(days=1)
        writer.writerow([next_number, date_string, reason])



