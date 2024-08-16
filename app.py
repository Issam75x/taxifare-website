import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import requests

st.write('Hey Taxi User :)')


st.markdown('''
Please fill the boxes to get your fare
''')

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

with st.form('Fill the boxes'):

    pick_up_date = st.date_input("Pick Up Date")
    pick_up_time = st.time_input("Pick Up Time",value=datetime.now().time())

    pickup_datetime = datetime.combine(pick_up_date,pick_up_time)
    pickup_longitude = st.number_input("Pickup Longitude")
    pickup_latitude = st.number_input("Pickup Latitude")
    dropoff_longitude = st.number_input("Dropoff Longitude")
    dropoff_latitude = st.number_input("Dropoff Latitude")
    passenger_count = st.number_input("Number of Passengers",min_value=1, max_value=7, value=1)


    submit_button = st.form_submit_button(label="Submit")

## Once we have these, let's call our API in order to retrieve a prediction




url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    params = dict({'pickup_datetime':pickup_datetime,
             'pickup_longitude':pickup_longitude,
             'pickup_latitude':pickup_latitude,
             'dropoff_longitude':dropoff_longitude,
             'dropoff_latitude':dropoff_latitude,
             'passenger_count':passenger_count})

result = requests.get(url,params)
y_pred = result.json()
st.write(y_pred)
