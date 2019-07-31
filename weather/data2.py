# Takes the 450th-550th entries in combinedData.csv and adds the weather data, and outputs it to combinedWeatherData2.csv
# Dark Sky api key required

import forecastio
from datetime import datetime, timedelta
import csv

api_key = ""

### ---------------------------------------------------
### 0: Regular Day 1: Snowday 2: Delay 3: Early Closing
### ---------------------------------------------------

### -------------------
### WRITE HEADER TO CSV
### -------------------

file = open('combinedWeatherData2.csv', 'w');
writer = csv.writer(file)

entries = 25

labels = []

for x in range(0, entries):
    labels.append("windGust" + str(x)) #
for x in range(0, entries):
    labels.append("temperature" + str(x))
for x in range(0, entries):
    labels.append("dewPoint" + str(x))  #
for x in range(0, entries):
    labels.append("humidity" + str(x)) #
for x in range(0, entries):
    labels.append("apparentTemperature" + str(x))
for x in range(0, entries):
    labels.append("pressure" + str(x)) #
for x in range(0, entries):
    labels.append("windSpeed" + str(x)) 
for x in range(0, entries):
    labels.append("visibility" + str(x)) #
for x in range(0, entries):
    labels.append("precipIntensity" + str(x))
for x in range(0, entries):
    labels.append("precipProbability" + str(x))

labels.append("day")
labels.append("month")


labels.append("outcome")

writer.writerow(labels)


### ----------------------------
### GET WEATHER DATA FOR 1 EVENT
### ----------------------------


def writeEvent(lat, lng, year, month, day, outcome):

    lat = lat
    lng = lng

    year = year
    month = month
    day = day

    outcome = outcome

    windGust = []
    temperature = []
    dewPoint = []
    humidity = []
    apparentTemperature = []
    pressure = []
    windSpeed = []
    visibility = []
    precipIntensity = []
    precipProbability = []

    # Day before from 2pm - midnight



    date = datetime(year, month, day) - timedelta(1)
    forecast = forecastio.load_forecast(api_key, lat, lng, time=date, units="us")
    

    h = forecast.hourly()

    
    for y in range(14, 24):
        if (len(h.data) <= y):
            print("Not enough data for " + str(month) + "/" + str(day - 1) + "/" + str(year))
            return

        data = h.data[y].d

        x = data.get('windGust', "none")
        if (x == "none"):
            x = 0
            print("No data for windGust for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        windGust.append(x)

        x = data.get('temperature', "none")
        if (x == "none"):
            x = 40
            print("No data for temperature for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        temperature.append(x)

        x = data.get('dewPoint', "none")
        if (x == "none"):
            x = 35
            print("No data for dewPoint for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        dewPoint.append(x)

        x = data.get('humidity', "none")
        if (x == "none"):
            x = .5
            print("No data for humidity for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        humidity.append(x)

        x = data.get('apparentTemperature', "none")
        if (x == "none"):
            x = 40
            print("No data for apparentTemperature for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        apparentTemperature.append(x)

        x = data.get('pressure', "none")
        if (x == "none"):
            x = 1013
            print("No data for pressure for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        pressure.append(x)

        x = data.get('windSpeed', "none")
        if (x == "none"):
            x = 1
            print("No data for windSpeed for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        windSpeed.append(x)

        x = data.get('visibility', "none")
        if (x == "none"):
            x = 9.997
            print("No data for visibility for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        visibility.append(x)

        x = data.get('precipIntensity', "none")
        if (x == "none"):
            x = 0
            print("No data for precipIntensity for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        precipIntensity.append(x)

        x = data.get('precipProbability', "none")
        if (x == "none"):
            x = 0
            print("No data for precipProbability for "  + str(month) + "/" + str(day - 1) + "/" + str(year) + " Hour " + str(y))
        precipProbability.append(x)

    # Day of from midnight to 3 pm

    date = datetime(year, month, day)
    forecast = forecastio.load_forecast(api_key, lat, lng, time=date, units="us")
    h = forecast.hourly()

    for y in range(0, 15):

        if (len(h.data) <= y):
            print("Not enough data for " + str(month) + "/" + str(day) + "/" + str(year) + str(y))
            return

        data = h.data[y].d

        x = data.get('windGust', "none")
        if (x == "none"):
            x = 0
            print("No data for windGust for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        windGust.append(x)

        x = data.get('temperature', "none")
        if (x == "none"):
            x = 40
            print("No data for temperature for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        temperature.append(x)

        x = data.get('dewPoint', "none")
        if (x == "none"):
            x = 35
            print("No data for dewPoint for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        dewPoint.append(x)

        x = data.get('humidity', "none")
        if (x == "none"):
            x = .5
            print("No data for humidity for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        humidity.append(x)

        x = data.get('apparentTemperature', "none")
        if (x == "none"):
            x = 40
            print("No data for apparentTemperature for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        apparentTemperature.append(x)

        x = data.get('pressure', "none")
        if (x == "none"):
            x = 1013
            print("No data for pressure for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        pressure.append(x)

        x = data.get('windSpeed', "none")
        if (x == "none"):
            x = 1
            print("No data for windSpeed for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        windSpeed.append(x)

        x = data.get('visibility', "none")
        if (x == "none"):
            x = 9.997
            print("No data for visibility for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        visibility.append(x)

        x = data.get('precipIntensity', "none")
        if (x == "none"):
            x = 0
            print("No data for precipIntensity for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        precipIntensity.append(x)

        x = data.get('precipProbability', "none")
        if (x == "none"):
            x = 0
            print("No data for precipProbability for "  + str(month) + "/" + str(day) + "/" + str(year) + " Hour " + str(y))
        precipProbability.append(x)

    # Write data to csv

    data = []
    data.extend(windGust)
    data.extend(temperature)
    data.extend(dewPoint)
    data.extend(humidity)
    data.extend(apparentTemperature)
    data.extend(pressure)
    data.extend(windSpeed)
    data.extend(visibility)
    data.extend(precipIntensity)
    data.extend(precipProbability)

    data.append(day)

    data.append(month)

    data.append(outcome)

    writer.writerow(data)

    print("Success for " + str(month) + "/" + str(day) + "/" + str(year))
    print(str(len(data)) + " data points")


end = csv.reader(open('combinedData.csv'))
lines = list(end)
length = len(lines)

for z in range(450, length):
    date = lines[z][0]
    outcome = int(lines[z][1])
    lat = float(lines[z][2])
    lon = float(lines[z][3])

    month, day, year = date.split('/')

    day = int(day)
    month = int(month)
    year = int(year)

    writeEvent(lat, lon, year, month, day, outcome)

    print("Number " + str(z) + " complete")



