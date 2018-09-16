from pullStockPriceHistory import *
from statistics import mean

print(stock_close_ordered_dict)
dictList = []
dates = []


for key in stock_close_ordered_dict:
    dates.append(key)
    dictList.append(stock_close_ordered_dict[key])

avgClosePrice = mean(dictList)
list_comparisons = list()
print(avgClosePrice)
for i in range(len(dictList)):
    percent_comparison = int((avgClosePrice - dictList[i])/avgClosePrice * 100)
    list_comparisons.append(percent_comparison)

# for key in stock_close_ordered_dict:
    # print(stock_close_ordered_dict[key])

print(dates)
print(type(dates[0]))
print(dictList)
print(list_comparisons)
