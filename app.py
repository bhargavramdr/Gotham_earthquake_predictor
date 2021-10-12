from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from tensorflow import keras
from sklearn.preprocessing import StandardScaler
import datetime
import time

app = Flask(__name__)

model = keras.models.load_model("Earthquake")
model.load_weights("weights.h5")


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Date = str(request.form['Date'])
        Time = str(request.form['Time'])
        Latitude = float(request.form['Latitude'])
        Longitude = float(request.form['Longitude'])

        # Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        # if(Fuel_Type_Petrol == 'Petrol'):
        #     Fuel_Type_Petrol = 1
        #     Fuel_Type_Diesel = 0
        # else:
        #     Fuel_Type_Petrol = 0
        #     Fuel_Type_Diesel = 1
        # Year = 2020-Year
        # Seller_Type_Individual = request.form['Seller_Type_Individual']
        # if(Seller_Type_Individual == 'Individual'):
        #     Seller_Type_Individual = 1
        # else:
        #     Seller_Type_Individual = 0
        # Transmission_Mannual = request.form['Transmission_Mannual']
        # if(Transmission_Mannual == 'Mannual'):
        #     Transmission_Mannual = 1
        # else:
        #     Transmission_Mannual = 0

        # sample = [[-29.400, -177.169, 42060.0]]

        try:
            ts = datetime.datetime.strptime(Date+' '+Time, '%m-%d-%Y %H.%M.%S')
            ts = (time.mktime(ts.timetuple()))
        except:
            # print('ValueError')
            ts = float(42060.0)

        sample = [[ts, Latitude, Latitude]]

        prediction = model.predict(sample)
        prediction = prediction.tolist()

        prediction_1 = round(prediction[0][0], 2)
        prediction_2 = round(prediction[0][1], 2)

        return render_template('index.html', prediction_texts="Magnitude:{} Richter magnitude".format(prediction_1), prediction_texts_1="Depth:{} km".format(prediction_2))

    #     if output < 0:
    #         return render_template('index.html', prediction_texts="Sorry you cannot sell this car")
    #     else:
    #         return render_template('index.html', prediction_text="You Can Sell The Car at {}".format(output))
    # else:
    #     return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
