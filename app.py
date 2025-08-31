import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.sav', 'rb'))

st.title("Airbnb Price Prediction")
st.write("Enter the details below to predict the price of airbnb.")    
neighbourhood_groups  = st.selectbox(
    "Neighbourhood group",options=['Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Bronx'],
    index=False
)
room_types= st.selectbox(
    "Room Type",options=['Private room', 'Entire home/apt', 'Shared room'],
    index=False
)
latitude = st.number_input("latitude", min_value=-100.0, max_value=200.0, value=5.0, format="%.5f")
longitude = st.number_input("longitude", min_value=-100.0, max_value=100.0, value=80.0, format="%.5f")
minimum_nights = st.number_input("minimum_nights", min_value=0, max_value=1000, value=10)
number_of_reviews = st.number_input("number_of_reviews", min_value=0, max_value=100, value=80)
reviews_per_month= st.number_input("reviews_per_month", min_value=0.0, max_value=20.0, value=5.0, format="%.2f")
calculated_host_listings_count = st.number_input("calculated_host_listings_count", min_value=0, max_value=100, value=80)
availability_365 = st.number_input("availability_365", min_value=0, max_value=400, value=2)
year = st.number_input("year", min_value=0, max_value=100000, value=5000)
month = st.number_input("month", min_value=0, max_value=1500000000, value=5000000)
day = st.number_input("day", min_value=0, max_value=50, value=10)
neigh_map={'Brooklyn':1, 'Manhattan':2, 'Queens':3, 'Staten Island':0, 'Bronx':4}
room_map={'Private room':1, 'Entire home/apt':0, 'Shared room':2}
neighbourhood_group=neigh_map[neighbourhood_groups]
room_type=room_map[room_types]
features = np.array([[neighbourhood_group, latitude, longitude,
                      room_type, minimum_nights, number_of_reviews, reviews_per_month,
                      calculated_host_listings_count, availability_365, year, month, day]
    ])

# Prediction
if st.button("Predict price of airbnb"):
    prediction = model.predict(features)
    predictions=np.expm1(prediction)
    st.success(f"Predicted price of airbnb: {predictions[0]:.2f}")
