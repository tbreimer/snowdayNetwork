# Creates 2017.csv, a list of all days in 2017, and what type of day they were in East Greenbush, NY, and including latitude and longitude.

import csv
from faker import Faker
from datetime import date, timedelta
import random

r = csv.reader(open('2017.csv'))
lines = list(r)
fake = Faker()

number = 0
start_date = date(year=2017, month=1, day=1)

for x in range (0, 365):
    date = start_date + timedelta(x)

    date = date.strftime('%m/%d/%y')
    print(date)

    lines.append([date, 0, 42.624511,-73.69084])
    
writer = csv.writer(open('2017.csv', "w"))
writer.writerows(lines)
