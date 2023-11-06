# class_ARIMA Documentation



## What is ARIMA?

   

     ARIMA, also known as Autoregressive Integrated Moving Average,

is a model created for time series analysis. Time series are variables that are recorded over time, an example is nominal GDP between 2008 and 2023.



    Models like ARIMA are backwards-looking projection models that estimate future values of a given variable by understanding the relation between past recorded instances of said variable. In this project, ARIMA is utilized to extrapolate the total population of the USA given historical data that begins from 1950 to 2023.





## Implementation of ARIMA



    In the code cell below, the necessary import statement and simple methodology of initializing a ARIMA container is presented. 

```python
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

data_dict = {'Year': [1950, 1951, ...., 2023]
             'TotalPopulation': [1*10^8, 1.5*10^8 ...., 3*10^8]}


data = pd.DataFrame(data_dict)
data = data.set_index('Year', 
inplace=True) # set index for ease of operation, not a necessity.

x_data = data['TotalPopulation'] # stores data that's for training
order = (1,1,0) # --> order = (p,d,q)
model = ARIMA(x_data,order=order) # initializes an instance of ARIMA

model_fit = model.fit() # fits data to model
```

### Variables

**data** -> DataFrame object that contains known observations for model training



**order** -> A tuple of 3-elements which are p, d and q respectively.

+ **p** = Number of autoregressive terms.

+ **d** = Number of differentiations applied on time series

+ **q** = Number of moving average terms
  
  

**x_data** -> Column of **data** that is subject to projection



**model** -> imported ARIMA class initialized with **x_data** and **order**.



**model_fit** -> fits data to the ARIMA model with respect to parameters specified in **order**. You can think of this as the method that trains the model.



## Making Predictions with ARIMA

    With a fitted model, making projections is quite simple. There is only one intermediary step to running the **predict()** method of ARIMA, which is, setting periods for the start and end of the duration we need the projections for.



```python
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


data_dict = {'Year': [2024, 2025, ...., 2101],
             'TotalPopulation': [3.1*10^8, 3.2*10^8 ...., 4.0*10^8]}
control_data = pd.DataFrame(data_dict) # Comparison data for ARIMA results.
control_data.set_index('Year', inplace=True)


start = control_data.index[0] # Start year of prediction
end = control_data.index[-1] # End year of prediction


predictions = model_fit.predict(start=start, end=end) # Make and store predictions
```

### Variables

**data_dict** -> Stores data that will compare to ARIMA projections



**control_data** -> DataFrame created from **data_dict**



**start** -> Starting index of projections, using the first index of **control_data** assures that projections will begin at the same period as the comparator dataset.



**end** -> Ending index of projection, using the last index of **control_data** assures that projections will end at the same period as the comparator dataset.



**predictions** -> array-like object that holds prediction values which can be accessed by using `predictions.values`. The index of said values, similarly, can be accessed by `predictions.index`






