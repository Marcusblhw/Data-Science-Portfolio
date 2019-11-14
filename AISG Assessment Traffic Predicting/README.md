# Traffic Volume Prediction MLP

This is an assessment for an AI accelerator programme where I had to explore a traffic dataset of an unidentified city in America. Afterwhich, I was tasked to create a machine learning pipeline (Took me some googling for this term, but it basically means a machine learning flow from start to end(what data to use, how are you going to split it, what machine learning method will you be using to train with the dataset)

This MLP uses a multivariate linear regression to predict the westbound traffic volume in a city. 

This module uses pandas, sklearn's linear regression & train test split, so make sure these modules are installed prior

##  How it works

The model is trained using the data set from: https://aisgaiap.blob.core.windows.net/aiap5-assessment-data/traffic_data.csv

The code replaces strings from the features holiday and weather_main into integers to be fed into the linear regression model.

predict_traffic.predict() takes 5 integer arguments (in order) which the linear regression model is trained on:
#### 1. holiday:

    None: 1,
    New Years Day: 2, 
    Washingtons Birthday: 3,
    Memorial Day: 4,
    Independence Day: 5,
    State Fair: 6,
    Labor Day: 7,
    Columbus Day: 8,
    Veterans Day: 9,
    Thanksgiving Day: 10,
    Christmas Day:11
     
     
#### 2. weather_main:

    Clouds: 1,
    Snow: 2,
    Clear: 3,
    Mist: 4,
    Haze: 5,
    Fog: 6,
    Rain: 7,
    Drizzle: 8,
    Thunderstorm: 9,
    Squall: 10


#### 3. month (1-12)
#### 4. day (1-31)
#### 5. time (0-23)

## How to use

```
import mlp.predict_traffic

predict_traffic.predict(holiday, weather_main, month, day, time)
```

### Example

To predict the traffic volume for a normal day, cloudy sky, June, 23rd, 2pm you write:
```
predict_traffic.predict(1, 1, 6, 23, 14)
```

And the algorithm will print out 

```
The predicted traffic volume on the 6/23 is: [number]
```


```python

```
## Reflection

This was tough because the assessment needed things and used jargons that were not within codeacademy's datascience programme (which is where I learnt data science). But with much googling and reading on stackoverflow, I learned things like creating my own functions and exporting them as my own .py file.
