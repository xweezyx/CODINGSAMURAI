#Importing libraries
from flask import Flask, render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('home.html')


@app.route("/predict",methods=['POST'])
def home():
    data_1 = float(request.form['sepal_length'])
    data_2 = float(request.form['sepal_width'])
    data_3 = float(request.form['petal_length'])
    data_4 = float(request.form['petal_width'])
    prediction_data = np.array([[data_1, data_2, data_3,data_4]])
    prediction = model.predict(prediction_data)
    return render_template("result.html",data=prediction)


if __name__ == '__main__':
    app.run(debug=True)