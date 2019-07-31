# Shuffles combinedDataNormalized.csv, outputs as combinedFinal.csv (Seen in network folder as train.csv)

import csv
import random

r = csv.reader(open('combinedDataNormalized.csv'))
lines = list(r)

newLines = []

finished = False

# Preserves dictionary lines as first line
firstLine = lines[0]
del lines[0]
newLines.append(firstLine)

while finished == False:
	rows = len(lines)
	
	index = random.randint(0, rows - 1)

	line = lines[index]

	newLines.append(line)

	del lines[index]

	newRows = len(lines)

	if (newRows == 0):
		finished = True

writer = csv.writer(open('combinedFinal.csv', "w"))
writer.writerows(newLines)
