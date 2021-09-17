import streamlit as st
from PIL import Image
import pandas as pd, numpy as np
import warnings
warnings.filterwarnings('ignore')

# image = Image.open(r"C:\Users\lordn\Downloads\c6e7dfb7c951eed5cb516b56a4751632.jpg")
# st.image(image, use_column_width=True)

st.write("""
Cars Price Prediction App

This is a simple app that estimates prices of cars to help arrive at fairer prcies in negotiations
""")

st.sidebar.header("Please input car data and features")

def car_input_features():
    brand = st.sidebar.text_input(label='Enter brand name')
    year = st.sidebar.number_input(label='Enter car model year')
    Km_driven = st.sidebar.number_input(label='Enter distance covered in lifetime (Km)')
    transmission = st.sidebar.selectbox('Please select transmission type',
              ("Automatic", 'Manual'))
    mileage = st.sidebar.number_input(label="Enter mileage (Kmpl) ")
    engine = st.sidebar.number_input(label="Enter engine capacity (cc) ")
    max_power = st.sidebar.number_input(label="Enter engine power rating (bhp) ")
    seats = st.sidebar.number_input(label="Enter number of seats in car")

    data = {"brand": brand,
                         "year": int(year),
                "km_driven": int(Km_driven),
                       "transmission": transmission,
            "mileage": float(mileage),
            "engine": float(engine),
            "max_power": float(max_power),
            "seats": int(seats)}

    return data

data = car_input_features()

def transform(data):
    cheap = ['Opel','Ambassador','Force','Toyota', 'Fiat','Nissan','Daewoo',
    'Renault','Volkswagen','Mitsubishi','Datsun','Chevrolet','Tata','Mahindra',
    'Ford','Hyundai','Honda','Skoda','Maruti', 'Kia', 'Peugeot']
    moderate = ['Jaguar', 'Opel', 'MG', 'Jeep', 'Land', 'Audi', 'Volvo', 'Benz']
    expensive = ['Lexus', 'BMW']
    data['brand'] = [0 if data['brand'].capitalize() in cheap else 1 if data['brand'].capitalize() in  moderate else 2 if data['brand'].capitalize() in expensive else 1][0]
    data['transmission'] = [0 if data['brand'] == 'Manual' else 1][0]
    return data

tranformed_data = transform(data)

data_df = pd.DataFrame(tranformed_data, index=[0])
data_array = np.array(data_df.values)


import joblib
model = joblib.load("car_price_estimator.pkl")

prediction = model.predict(data_array)

    
if st.sidebar.button("PREDICT"):
    st.subheader("Car Input Parameters")
    st.write(data_df)
    st.subheader("PREDICTION")
    st.write(f"The car you are looking to buy will cost you ${int(round(prediction[0]))}.\n Good luck raising the money!!")




