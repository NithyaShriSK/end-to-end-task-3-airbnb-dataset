import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.sav', 'rb'))

st.title("Airbnb Price Prediction")
st.write("Enter the details below to predict the price of airbnb.")    
neighbourhood_group  = st.number_input("neighbourhood_group ", min_value=0.0, max_value=1000.0, value=150.0, format="%.2f")
neighbourhood = st.number_input("neighbourhood", min_value=0, max_value=1000, value=10)
latitude = st.number_input("latitude", min_value=0.0, max_value=20.0, value=5.0, format="%.2f")
longitude = st.number_input("longitude", min_value=0.0, max_value=100.0, value=80.0, format="%.2f")
room_type  = st.number_input("room_type ", min_value=0, max_value=10000, value=50)
minimum_nights = st.number_input("minimum_nights", min_value=0, max_value=1000, value=10)
number_of_reviews = st.number_input("number_of_reviews", min_value=0.0, max_value=100.0, value=80.0, format="%.2f")
reviews_per_month= st.number_input("reviews_per_month", min_value=0.0, max_value=20.0, value=5.0, format="%.2f")
calculated_host_listings_count = st.number_input("calculated_host_listings_count", min_value=0.0, max_value=100.0, value=80.0, format="%.2f")
availability_365 = st.number_input("availability_365", min_value=0.0, max_value=100.0, value=0.5, format="%.2f")
year = st.number_input("year", min_value=0.0, max_value=100000.0, value=5000.0, format="%.2f")
month = st.number_input("month", min_value=0.0, max_value=1500000000.0, value=5000000.0, format="%.2f")
day = st.number_input("day", min_value=0.0, max_value=50.0, value=10.0, format="%.2f")

features = np.array([[neighbourhood_group, neighbourhood, latitude, longitude,
                      room_type, minimum_nights, number_of_reviews, reviews_per_month,
                      calculated_host_listings_count, availability_365, year, month, day]
    ])

# Prediction
if st.button("Predict price of airbnb"):
    prediction = model.predict(features)
    st.success(f"Predicted price of airbnb: {prediction[0]:.2f} years")
