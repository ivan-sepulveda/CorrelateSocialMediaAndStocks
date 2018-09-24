from pullStockPriceHistory import *
from statistics import mean
import alpha_vantage



def returnPercentChangesByDate(stock_close_ordered_dict):
    listPrices = []
    dates = []
    stockMetrics = dict()
    for key in stock_close_ordered_dict:
        dates.append(key)
        listPrices.append(stock_close_ordered_dict[key])
    avgPrice = mean(listPrices)
    list_comparisons = list()
    for i in range(len(listPrices)):
        percent_comparison = (listPrices[i]-avgPrice )/avgPrice * 100
        list_comparisons.append(percent_comparison)
    stockMetrics["prices"] = listPrices
    stockMetrics["price_percent_changes"] = list_comparisons
    stockMetrics["date_strings"] = dates
    return stockMetrics


# for key in stock_close_ordered_dict:
    # print(stock_close_ordered_dict[key])