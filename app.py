from fastapi import FastAPI, Request
import pandas as pd, numpy as np
import joblib
from zipfile import ZipFile

file_name = "model.zip"

with ZipFile(file_name, 'r') as file:
    model = joblib.load(file.open('car_price_estimator.pkl', 'r'))

app = FastAPI()

def transform(data):

    cheap = ['Opel','Ambassador','Force','Toyota', 'Fiat','Nissan','Daewoo',
    'Renault','Volkswagen','Mitsubishi','Datsun','Chevrolet','Tata','Mahindra',
    'Ford','Hyundai','Honda','Skoda','Maruti', 'Kia', 'Peugeot']
    moderate = ['Jaguar', 'Opel', 'MG', 'Jeep', 'Land', 'Audi', 'Volvo', 'Benz']
    expensive = ['Lexus', 'BMW']
    data['brand'] = [0 if data['brand'].capitalize() in cheap else 1 if data['brand'].capitalize() in  moderate else 2 if data['brand'].capitalize() in expensive else 1][0]
    data['transmission'] = [0 if data['brand'] == 'Manual' else 1][0]
    return data


@app.get('/')
def homepage():
    return "Welcome!!"



@app.post('/predict')

async def predict(request: Request):

    data = await request.json()

    tranformed_data = transform(data)

    data_df = pd.DataFrame(tranformed_data, index=[0])
    data_array = np.array(data_df.values)


    # model = joblib.load("car_price_estimator.pkl")
    prediction = model.predict(data_array)[0]

    response = {'PREDICTION': prediction}

    return response
