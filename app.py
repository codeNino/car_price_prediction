import streamlit as st, pandas as pd
from PIL import Image
import warnings, requests
warnings.filterwarnings('ignore')


image = Image.open(r"C:\Users\lordn\Downloads\c6e7dfb7c951eed5cb516b56a4751632.jpg")
st.image(image, use_column_width=True)  

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
    seats = st.sidebar.slider(label="Number of seats in car", min_value=1 , max_value=10, step=1)
    
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

result = requests.post('http://127.0.0.1:8000/predict', json=data)

data_df = pd.DataFrame(data, index=[0])
prediction = result.json()["PREDICTION"]

    
if st.sidebar.button("PREDICT"):
    st.subheader("Car Features")
    st.write(data_df)
    st.subheader("PREDICTION")
    st.write(f"The car you are looking to buy will cost you ${int(round(prediction))}.\n Good luck raising the money!!")
