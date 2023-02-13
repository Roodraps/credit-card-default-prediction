import pickle
from flask import Flask,jsonify,request,app,render_template
import numpy as np 
import pandas as pd 
from xgboost import XGBClassifier


app = Flask(__name__)                         # creating the flask app from where our app will run

# load the model
xgbmodel = pickle.load(open("model_xgboost_oversampling.pkl","rb"))

@app.route('/')
def home():
    return render_template('home.html')   # this will redirect to the home page of html


@app.route("/predict_api",methods = ['POST'])  # this is for api testing
def predict_api():
    data = request.json['data']
    new_data = (np.array(list(data.values()))).reshape((1,-1))
    
    prediction = xgbmodel.predict(new_data)
    print("prediction", prediction)
    
    if prediction == 0:
      return "non_fradulent"
    elif prediction == 1:
        return "fraudulent"

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    new_data = np.array(data).reshape(1,-1)
    output = xgbmodel.predict(new_data)
    if output == 0:
      return " RELIEF! This person is non fraudulent"
    elif output == 1:
        return " DANGER! This person is fraudulent"
    # return render_template("home.html",prediction_text="He is a {}".format(output))
    



if __name__ == " __main__ ":
    app.run(debug = True) 

