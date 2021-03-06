# Does the NYSE have an API?
from alpha_vantage.alpha_vantage import timeseries
from datetime import date
from datetime import datetime
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
import calendar
from collections import OrderedDict, defaultdict

"""
@:param stock_price
alpha_vantage gives us a variety of options for obtaining the stock price of an index for a given day. They must be
entered as follows. 
 
Stock Opening Price: stock_price =  "1. open"
Stock Daily High: stock_price =  "2. high"
Stock Daily Low: stock_price =  "3. low"
Stock Closing Price: stock_price =  "4. close"

@:param volume
If you would instead like to pull the volume of that retailers stocks traded that day you can either enter into params
stock_price =  "5. volume", or set volume=True.
"""
def pullStockPriceHistoryData(alphaVantageKey, nasdaqIndex, stock_price="4. close", series = "daily"):
    ts = timeseries.TimeSeries(key=alphaVantageKey, output_format='pandas')
    if series == "daily":
        # data, meta_data = ts.get_daily(symbol=nasdaqIndex, outputsize="full")
        data, meta_data = ts.get_daily(symbol=nasdaqIndex, outputsize="compact")
    if series == "weekly":
        data, meta_data = ts.get_weekly(symbol=nasdaqIndex)
    if series == "monthly":
        data, meta_data = ts.get_monthly(symbol=nasdaqIndex)
    # print(data)
    edited_data = pd.DataFrame(data)
    stock_close = edited_data[stock_price]
    # print(type(edited_data["1. open"]))
    stock_close_ordered_dict = stock_close.to_dict(OrderedDict)
    return stock_close_ordered_dict


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


