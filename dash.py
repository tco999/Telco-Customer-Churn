from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('home.html')

# About Page
@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

# Dataset Page
@app.route('/database', methods=['POST', 'GET'])
def dataset():
    return render_template('dataset.html')

# Visualization Page
@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

# Prediction Page
@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    return render_template('predict.html')

# Result Page
@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df_predict = pd.DataFrame({
            'Gender':[input['Gender']],
            'SeniorCitizen':[input['SeniorCitizen']],
            'Partner':[input['Partner']],
            'Dependents':[input['Dependents']],
            'Tenure':[input['Tenure']],
            'MultipleLines':[input['MultipleLines']],
            'InternetService':[input['InternetService']],
            'OnlineSecurity':[input['OnlineSecurity']],
            'OnlineBackup':[input['OnlineBackup']],
            'DeviceProtection':[input['DeviceProtection']],
            'TechSupport':[input['TechSupport']],
            'StreamingTV':[input['StreamingTV']],
            'StreamingMovies':[input['StreamingMovies']],
            'Contract':[input['Contract']],
            'PaperlessBilling':[input['PaperlessBilling']],
            'PaymentMethod':[input['PaymentMethod']],
            'MonthlyCharges':[input['MonthlyCharges']],          
            
        })

        prediksi = model.predict_proba(df_predict)[0][1]

        if prediksi > 0.5:
            churn = "Your Customer is Going to Churn! Act Fast!"
        else:
            churn = "Your Customer is Going to Stay! Keep up the Good Work!"

        return render_template('result.html',
            data=input, pred=churn)

if __name__ == '__main__':

    filename = 'model.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)