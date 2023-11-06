import pandas as pd
import numpy as np

import datetime as dt

from statsmodels.tsa.arima.model import ARIMA

class ARIMA_container():
    def __init__(self, data, order=(1,1,0)) -> None:
        
        self.data = data
        
        self.control_data = None
        self.training_data = None
        
        self.pdq = (13,1,0)
        
        self.predictions = order
        
    def data_prep(self) -> None:
    
        control_data = self.data.loc[self.data['Time'] >= '2024-01-01', ['Time', 'TPopulation1Jan']]
        control_data.set_index('Time', inplace=True)
        control_data = control_data.asfreq('AS-JAN')
        
        self.control_data = control_data

        training_data = self.data.loc[self.data['Time'] <= '2023-01-01', ['Time', 'TPopulation1Jan']]
        training_data.set_index('Time', inplace=True)
        training_data = training_data.asfreq('AS-JAN')
        
        self.training_data = training_data
        
    def estimate(self, order: tuple=(13,1,0)) -> None:
        
        self.data_prep()
        
        model = ARIMA(self.training_data['TPopulation1Jan'], order=self.pdq)
        model_fit = model.fit()
        
        start = self.control_data.index[0]
        end = self.control_data.index[-1]
        
        predictions = model_fit.predict(start=start, end=end)
        self.predictions = predictions