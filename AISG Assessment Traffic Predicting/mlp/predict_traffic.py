#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://aisgaiap.blob.core.windows.net/aiap5-assessment-data/traffic_data.csv')
split_df = df['date_time'].str.split('(\d+)', expand=True)
df['month'] = pd.to_numeric(split_df[3])
df['day'] = pd.to_numeric(split_df[5])
df['time'] = pd.to_numeric(split_df[7])

#Change string data in holiday & weather_main features into integers to be used in MLR later.
df.holiday = df.holiday.replace({"None": "1", 
                                 "New Years Day": "2", 
                                 "Washingtons Birthday": "3",
                                 "Memorial Day" : "4",
                                 'Independence Day':'5',
                                 'State Fair':'6',
                                 'Labor Day':'7',
                                 'Columbus Day':'8',
                                 'Veterans Day':'9',
                                 'Thanksgiving Day':'10',
                                 'Christmas Day':'11'
                                })
df['holiday']=pd.to_numeric(df.holiday)

df.weather_main = df.weather_main.replace({'Clouds':'1',
                                 'Snow':'2',
                                 'Clear':'3',
                                 'Mist':'4',
                                 'Haze':'5',
                                 'Fog':'6',
                                 'Rain':'7',
                                 'Drizzle':'8',
                                 'Thunderstorm':'9',
                                 'Squall':'10'
                                })
df['weather_main']=pd.to_numeric(df.weather_main)

def predict(holiday, weather_main, month, day, time):
    x = df[['holiday', 'weather_main','month', 'day', 'time']]
    y = df['traffic_volume']
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

    mlr = LinearRegression()
    mlr.fit(x_train, y_train) 

    y_predicted = mlr.predict(x_test)

    variables = [[holiday, weather_main, month,day, time]]

    predict = mlr.predict(variables)

    print('The predicted traffic volume on the {}/{} is:{}'.format(day, month, predict))

