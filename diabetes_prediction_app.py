import streamlit as st
from PIL import Image
import pandas as pd, numpy as np
import warnings
warnings.filterwarnings('ignore')

#image = Image.open(r"C:\Users\lordn\Downloads\diabetes_treat.jpg")
#st.image(image, use_column_width=True)

st.write("""

Diabetes likelihood Prediction App

An AI enabled application that predicts the likelihood of patients being diabetic.
Note: All predictions are non conclusive nor final.

""")

st.sidebar.header("Please input patient data and features")

def user_input_features():
    pregnancies = st.sidebar.number_input(label='Enter pregnancies frequency')
    glucose = st.sidebar.number_input(label='Enter glucose level')
    bloodpressure = st.sidebar.number_input(label='Enter blood pressure')
    age = st.sidebar.number_input(label='Enter Age')

    data = {"Pregnancies": pregnancies,
    "Glucose": glucose,
    "Blood Pressure": bloodpressure,
    "Age": age}

    return data

data = user_input_features()
data_df = pd.DataFrame(data,index=[0])
data_array = np.array(data_df.values)

st.subheader("User Input Parameters")
st.write(data_df)

import joblib
model = joblib.load("diabetes_predictor.pkl")
prediction = model.predict(data_array)

def output(pred):
    if pred == 0:
        print("Likelihood of diabetes for patient is negative.")
    else:
        print("Likelihood of diabetes for patient is positive. \n Please make recommendations!")

st.subheader("PREDICTION")
st.write(output(prediction))

st.subheader("MODEL CONFIDENCE")
st.write(model.predict_proba(data_array))

