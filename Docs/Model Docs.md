# Model Documentation

## Variable List

| **Name**          | **Type**        | **Description**                                                                              | **Reference**                                                                                           |
| ----------------- | --------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| simple_cols       | List            | Columns to keep in **simple_raw_data**                                                       | [Python docs](https://docs.python.org/3/tutorial/datastructures.html)                                   |
| simple_raw_data   | pd.DataFrame    | Stores variables to be used in  ARIMA projection without filtration.                         | [Pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)                       |
| simple_data_usa   | pd.DataFrame    | Stores columns of **simple_raw_data** filtered to display information about USA.             | [Pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)                       |
| ARIMA             | ARIMA_container | Imported from *"/class_ARIMA.py"*. Holds an ARIMA model with **simple_data** as its dataset. | [Statsmodels docs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html) |
| complex_drop_cols | List            | Columns to drop from **complex_raw_data**                                                    | [Python docs](https://docs.python.org/3/tutorial/datastructures.html)                                   |
| complex_raw_data  | pd.DataFrame    | Stores variables for projection methods that can utilize all 55 variables of the dataset.    | [Pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)                       |
| complex_data_usa  | pd.DataFrame    | Stores columns of **complex_raw_data** filtered to display information about USA.            | [Pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)                       |

## Methodology for ARIMA

    See "\class_ARIMA Docs.md" for step by step breakdown of ARIMA implementation in this project. Refer to [Statsmodels docs](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html) for a more detailed documentation.

## Data Vizualization

    Matplotlib's pyplot module is used for plotting in this project, please refer to [Matplotlib docs](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot) for detailed explanation of all methods and parameters used for vizualization in this project.
