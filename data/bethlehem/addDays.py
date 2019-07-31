
import csv
from faker import Faker
import datetime
import random

r = csv.reader(open('bethlehem.csv'))
lines = list(r)
fake = Faker()

number = 0

while number < 35:

    start_date = datetime.date(year=2009, month=11, day=15)
    end_date = datetime.date(year=2010, month=3, day=4)

    date = fake.date_between(start_date=start_date, end_date=end_date)

    year = str(random.randint(2009, 2019))

    date = date.strftime('%m/%d/' + year)

    snowdays = [row[0] for row in lines]

    if date in snowdays:
        pass
    else:
        lines.append([date, 0, 42.610909,-73.855721])
        number = number + 1

number = 0

while number < 8:

    start_date = datetime.date(year=2009, month=3, day=4)
    end_date = datetime.date(year=2009, month=11, day=15)

    date = fake.date_between(start_date=start_date, end_date=end_date)

    year = str(random.randint(2009, 2019))

    date = date.strftime('%m/%d/' + year)

    snowdays = [row[0] for row in lines]

    if date in snowdays:
        print(date + "Already in dateset")
    else:
        lines.append([date, 0, 42.610909,-73.855721])
        number = number + 1


writer = csv.writer(open('bethlehem.csv', "w"))
writer.writerows(lines)
