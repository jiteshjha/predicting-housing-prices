import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

def get_data(file_name):
    data = pd.read_csv(file_name)
    x = []
    y = []
    for i, j in zip(data['x'], data['y']):
        x.append([float(i)])
        y.append([float(j)])

    return x, y

def linear_model_main(x, y, predict_value):
    regression = linear_model.LinearRegression()
    regression.fit(x, y)
    predict_outcome = regression.predict(predict_value)
    predictions = {}
    predictions['theta0'] = regression.intercept_
    predictions['theta1'] = regression.coef_
    predictions['predict_value'] = predict_outcome
    return predictions



x,y = get_data('input_data.csv')
predict_value = data = input("Enter value to predict: ")
result = linear_model_main(x, y, predict_value)
print "Predicted value: ", result['predict_value'][0][0]
