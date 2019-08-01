# snowdayNetwork

This is a program that trains a neural network to predict snowdays, 2hr delays and early closings of schools based on weather using TensorFlow. If you wish to see it train on your computer quickly, go to Quick Start below. If you would like to know the steps and process I took in the creation of this project, jump to Process.


## Quick Start
* Ensure that TensorFlow version 1.14.0 is installed
* Navigate to /network/
* Run snowDay.py using python

## Process

### Collecting the Raw Data

Before starting the project, adequate data had to be collected. The data needed to consist of hundreds of examples of snowdays, 2hr delays, and early closings. In order to mitigate the effect of variables such as state, region, and school type, Only suburban, public districts in the capital region of New York State were selected. These districts were East Greenbush, Bethlehem, Saratoga, Schodack, and Shenendehowa. The data was retrieved through the disticts' Facebook pages or by requesting it from the school's superintendent, and it goes back about a decade. The raw file for each school can be found in /data/ in the district's folder in an .ods format. It includes the date, what event occurred that day (0: Regular Day, 1; Snowday, 2: 2hr Delay, 3: Early Closing), the latitude, and the longitude of the district.

### Adding Regular Days

In order for the network to discern between normal days and "events" such as snowdays, 2hr delays and early closings, regular days had to be added into the data. This was done using the file addDays.py located in the folder of each distict in /data/, creating the .csv file. Most of the normal days added were days from Novemeber to March, as events outside this range are rare; it is important for the network to discern the difference between a regular winter day and one on which an event occurs. This addition of regular days increased the size of the data by about 250%. This high number was chosen since events are much more rare than regular days, and it is neccessary for the training data to reflect that. In the folder /data/total/, the combination of all the data can be found as total.csv.

### Retrieving the Weather Data

Now that the days that the network would be training on were set, the weather data for each one had to be retrieved, thus creating the training data for the network. This step was done for each day using [Dark Sky's API](https://darksky.net/dev). In /weather/, the data.py and data2.py allow for the the combinedData.csv file to be split after 450 days, and the weather data is outputted separately in two combinedWeatherData.py files. For each day, 10 weather measureables were added on an hourly basis over 25 hours, from 2pm the day before to 3pm the day of. This was done as the weather the day before can influence a district's descision to close, while the weather after school has ended does not. The data included was wind gust, temperature, dew point, humidity, apparent temperature, pressure, wind speed, visibility, precipitation intensity, and precipitation probability. Each of these measureables over 25 hours plus the day and month combined for 252 data points for each day.

### Data Pre-Processing

Before the data was fed through the network for training, it had to be normalized. This was done on a scale from 0-1 for each weather measureable based upon a pre-defined range. This way, training data, testing data, and predicition data could all be normalized on the same scale. Normalization was done using normalize.py in /weatherProcessing/, creating the file combinedDataNormalized.csv. Finally, the data was shuffled randomly to prevent the network from shifting in a particular direction when it was training on a specific area of the data. This was done using shuffle.py, creating the file combinedFinal.csv from combinedDataNormalized.csv. Thus, the training data was ready.

### Testing Data

In order to test the network, all of East Greenbush's data from 2017 was taken out of the training data. In /2017/, addDays.py creates 2017.csv, a list of all the days in 2017, what kind of day it was (0, 1, 2, 3: days other than 0 were manually subed in)



Powered by Dark Sky









