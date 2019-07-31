
import csv
from faker import Faker
import datetime
import random

r = csv.reader(open('saratoga.csv'))
lines = list(r)
fake = Faker()

number = 0

while number < 55:

    start_date = datetime.date(year=2009, month=11, day=15)
    end_date = datetime.date(year=2010, month=3, day=4)

    date = fake.date_between(start_date=start_date, end_date=end_date)

    year = str(random.randint(2009, 2019))

    date = date.strftime('%m/%d/' + year)

    snowdays = [row[0] for row in lines]

    if date in snowdays:
        print(date + "Already in dateset")
    else:
        lines.append([date, 0, 43.07425,-73.800390])
        number = number + 1

number = 0

while number < 15:

    start_date = datetime.date(year=2009, month=3, day=4)
    end_date = datetime.date(year=2009, month=11, day=15)

    date = fake.date_between(start_date=start_date, end_date=end_date)

    year = str(random.randint(2009, 2019))

    date = date.strftime('%m/%d/' + year)

    snowdays = [row[0] for row in lines]

    if date in snowdays:
        print(date + "Already in dateset")
    else:
        lines.append([date, 0, 43.07425, -73.800390])
        number = number + 1


writer = csv.writer(open('saratoga.csv', "w"))
writer.writerows(lines)
