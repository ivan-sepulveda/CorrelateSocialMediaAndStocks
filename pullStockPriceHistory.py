# Does the NYSE have an API?
from alpha_vantage.alpha_vantage import timeseries
from datetime import date
from datetime import datetime
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
import calendar
from collections import OrderedDict, defaultdict

ts = timeseries.TimeSeries(key='HQXQHIFN548EZELL', output_format='pandas')

# data, meta_data = ts.get_intraday(symbol='NKE',interval='1min', outputsize='full')
data, meta_data = ts.get_daily(symbol='NKE')
# print(data)
edited_data = pd.DataFrame(data)
stock_close = edited_data["4. close"]
# print(type(edited_data["1. open"]))
stock_close_ordered_dict = stock_close.to_dict(OrderedDict)

def convert_str_to_date(strr):
    year = strr[:4]
    month = strr[5:7]
    monthStrAbbrv = calendar.month_abbr[int(month)]
    # print(calendar.month_abbr[int(month)])
    day = strr[-2:]
    # print(day)

    item3 = datetime.strptime('{0} {1} {2}  4:00PM'.format(monthStrAbbrv, day, year), '%b %d %Y %I:%M%p')
    # converting back to simple date
    item3 = item3.date()
    return item3
    # stock_close_ordered_dict_b[item3] =
    # print(key, stock_close_ordered_dict[key])
    # print(key," - " ,item3)
    # stock_close_ordered_dict_b[item3] = stock_close_ordered_dict[key]



# print(stock_close.to_dict(OrderedDict))

# print(edited_data['2018-09-11'].values.tolist())
 # = pd.Data['2018-09-11'].values.tolist()

# data['4. close'].plot()
# plt.title('Intraday Times Series for the NKE stock (1 min)')
# plt.xlabel(date.today())
# plt.show()

