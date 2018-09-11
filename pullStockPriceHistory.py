# Does the NYSE have an API?
from alpha_vantage.alpha_vantage import timeseries
from datetime import date
from pprint import pprint
import matplotlib.pyplot as plt
ts = timeseries.TimeSeries(key='HQXQHIFN548EZELL', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='NKE',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the NKE stock (1 min)')
plt.xlabel(date.today())
plt.show()

