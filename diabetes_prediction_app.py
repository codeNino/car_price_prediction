import streamlit as st
from PIL import Image
import pandas as pd, numpy as np
import warnings
warnings.filterwarnings('ignore')

#image = Image.open(r"C:\Users\lordn\Downloads\diabetes_treat.jpg")
#st.image(image, use_column_width=True)

st.write("""

Diabetes likelihood Prediction App

This is a simple app to check the likelihood of diabetes in patients

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

import joblib
model = joblib.load("diabetes_predictor.pkl")

prediction = model.predict(data_array)

confidence = model.predict_proba(data_array)
confidence = pd.Series(confidence[0], index=['Negative',"Positive"])


def output(pred):
    if pred == 0:
        return "Likelihood of diabetes for patient is negative."
    
    else:
        return "Likelihood of diabetes for patient is positive. \n Please make recommendations!"


if st.sidebar.button("PREDICT"):
    st.subheader("User Input Parameters")
    if st.button("VIEW"):
        st.write(data_df)
    
    st.subheader("PREDICTION")
    st.write(output(prediction))
    
    st.subheader("MODEL CONFIDENCE")
    if st.button("CHECK"):
        st.write(confidence)








