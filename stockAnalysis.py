from pullStockPriceHistory import *
from statistics import mean
import alpha_vantage
from initialConditions import *
from datetime import datetime
from datetime import timedelta
import calendar



def returnPercentChangesByDate(stock_close_ordered_dict, avg = "all"):
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

def roundToNearestFriday(dateString):
    # we always round up
    # in the future, it might be a good ida to look at times
    # if nike posted a photo friday at 8pm EST, the market already closed, but the post might affect next weeks market
    # Although I acknowledge that friday might now be the last trading day due to holidays
    datetimeDate = datetime.strptime(dateString+'  1:33PM', '%Y-%m-%d %I:%M%p').date()
    weekdayWeekendInteger = datetimeDate.weekday()
    daysToAdd = 0
    roundedDate = datetimeDate
    # according to calendar.day_name, indexing starts with Monday at index 0
    # so if weekday_integer < 4, we'll add add number to get to Friday
    # so if weekday_integer is > 4, we assume that the market already close and the post wont affect the market until
    # the NEXT Friday
    # print("weekday integer", datetimeDate.weekday())
    if weekdayWeekendInteger < 4:
        while roundedDate.weekday() != 4:
            daysToAdd += 1
            roundedDate = datetimeDate + timedelta(days=daysToAdd)
    if weekdayWeekendInteger > 4:
        while roundedDate.weekday() != 4:
            daysToAdd += 1
            roundedDate = datetimeDate + timedelta(days=daysToAdd)
            # print(roundedDate.weekday())

    # print(roundedDate)
        # print(calendar.day_name[weekdayWeekendInteger])
        # print(datetimeDate + timedelta(days=1))
    # if weekdayWeekendInteger > 4:
    #     print(calendar.day_name[weekdayWeekendInteger])

    print("input date is {0} and falls on a {1}".format(datetimeDate, calendar.day_name[datetimeDate.weekday()]))
    # Friday
    return roundedDate

def percentChangesByDayScaled(stock_close_ordered_dict, scaleInterval):
    print("starting: percentChangesByDayScaled(nasdaqDataDaily, 'weekly)")
    scaleByThisSeries = pullStockPriceHistoryData(av_key, retailerNasdaq, series=scaleInterval)
    # print(" okay let me see what dates are in the weekly series")
    # print(scaleByThisSeries)
    listPrices = []
    dates = []
    stockMetrics = dict()
    count1 = 0
    count2 = 0


    print("Stock Price, Date")
    for key in stock_close_ordered_dict:
        count1 += 1
        dates.append(key)
        listPrices.append(stock_close_ordered_dict[key])
        if count1 < 5:
            print(stock_close_ordered_dict[key], key)

    avgPrice = mean(listPrices)
    print("\navg over all time: ", avgPrice)
    print("overAllTime, By Week")
    list_comparisons = list()
    listIntervalComparisons = list()

    for i in range(len(listPrices)):
        count2 += 1
        percent_comparison = (listPrices[i]-avgPrice)/avgPrice * 100
        list_comparisons.append(percent_comparison)
        roundedToFriday = roundToNearestFriday(dates[i])
        weeklyAvg = scaleByThisSeries[str(roundedToFriday)]
        percentComparisonToInterval = (listPrices[i] - weeklyAvg) / weeklyAvg * 100
        listIntervalComparisons.append(percentComparisonToInterval)
        if count2 < 5:
            print(percent_comparison, 0)
            print("date again: ", dates[i])
            print("Let's try rounding this to the nearest end of week trading day (Friday if non-holiday)")
            print("lets check if our round to friday returns a stock data point below")
            print(scaleByThisSeries[str(roundedToFriday)], type(scaleByThisSeries[str(roundedToFriday)]))
            print("Percent Comparison to Weekly Avg: ", percentComparisonToInterval)
            # print(scaleByThisSeries[roundedToFriday])
    stockMetrics["prices"] = listPrices
    stockMetrics["price_percent_changes"] = list_comparisons
    stockMetrics["price_percent_changes_"+scaleInterval] = list_comparisons

    stockMetrics["date_strings"] = dates
    return stockMetrics




# for key in stock_close_ordered_dict:
    # print(stock_close_ordered_dict[key])