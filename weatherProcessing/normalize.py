# Normalizes combinedWeatherData.csv from 0-1, outputs as combinedDataNormalized.csv

import csv

r = csv.reader(open('combinedWeatherData.csv'))
lines = list(r)


row_count = 550


# windGust
mn = 0
mx = 40

for x in range(0, 25):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# temperature
mn = -30
mx = 120

for x in range(25, 50):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# dewPoint
mn = -30
mx = 120

for x in range(50, 75):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# humidity
mn = 0
mx = 1

for x in range(75, 100):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# apparentTemperature
mn = -30
mx = 120

for x in range(100, 125):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)
		
		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# pressure
mn = 975
mx = 1050

for x in range(125, 150):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# windSpeed
mn = 0
mx = 20

for x in range(150, 175):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))
# visibility
mn = 0
mx = 10

for x in range(175, 200):

	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# precipIntensity
mn = 0
mx = .5

for x in range(200, 225):
	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

# precipProbability
mn = 0
mx = 1

for x in range(225, 250):
	c = [item[x] for item in lines]

	del c[0]

	for y in range(1, row_count):
		num = float(lines[y][x])

		val = (num - mn) / (mx - mn)


		lines[y][x] = str(val)

		if (val > 1 or val < 0):
			name = lines[0][x]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))

mn = 1
mx = 31

for y in range(1, row_count):
	num = float(lines[y][250])

	val = (num - mn) / (mx - mn)


	lines[y][250] = str(val)

	if (val > 1 or val < 0):
			name = lines[0][25]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))
0
mn = 1
mx = 12

for y in range(1, row_count):
	num = float(lines[y][251])

	val = (num - mn) / (mx - mn)


	lines[y][251] = str(val)


	if (val > 1 or val < 0):
			name = lines[0][251]
			print("Out of bounds value at " + str(name) + " " + str(y + 1))





writer = csv.writer(open('combinedDataNormalized.csv', "w"))
writer.writerows(lines)

