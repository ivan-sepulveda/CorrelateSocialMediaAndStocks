from pullStockPriceHistory import *
from statistics import mean
import alpha_vantage
from initialConditions import *
from datetime import datetime
from datetime import timedelta
import calendar
import holidays

print("testing us holidays")
print(date(2012, 1, 1) in holidays.US())
print(holidays.US().items())
for date, name in sorted(holidays.US().items()):
    print(date, name)
# import urllib2

def main():
    req = urllib2.Request('https://api.tradier.com/v1/user/profile')
    req.add_header('Authorization', 'Bearer YOUR_ACCESS_TOKEN')
    f = urllib2.urlopen(req)
    print(f.read())


def returnPercentChangesByDate(stock_close_ordered_dict, avg = "all"):
    listPrices = []
    dates = []
    stockMetrics = dict()
    instagramFoundDate = datetime(2010, 10, 6).date()
    for key in stock_close_ordered_dict:
        if stringToDatetimeDate(key) > instagramFoundDate:

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

def roundToLastTradingDay(dateRoundedToFriday):
    if dateRoundedToFriday in holidays.UnitedStates():
        if  holidays.US().get(dateRoundedToFriday) == "New Year's Day (Observed)":
            return dateRoundedToFriday
        # if  holidays.US().get(dateRoundedToFriday) == "Veterans Day":
        #     print("new year homie")
        #     print(holidays.US().get(date(2012, 12, 25)))
        #     return dateRoundedToFriday + timedelta(1)
        # I dont' know why april 22nd return an error
        # but the alpha vantage time series says that their weekly average comes from 4-21
        if dateRoundedToFriday == date(2011, 4, 22):
            return date(2011, 4, 21)
        print("{0} is a holiday!".format(dateRoundedToFriday))
        print("Here's the list actually")
        print(holidays.US().get_list(dateRoundedToFriday))
        return dateRoundedToFriday - timedelta(1)
    else:
        return dateRoundedToFriday



def roundToNearestFriday(dateString):
    print("input date is "  + dateString)
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

    # print("input date is {0} and falls on a {1}".format(datetimeDate, calendar.day_name[datetimeDate.weekday()]))
    # Friday
    return roundedDate

def stringToDatetimeDate(dateString):
    # we always round up
    # in the future, it might be a good ida to look at times
    # if nike posted a photo friday at 8pm EST, the market already closed, but the post might affect next weeks market
    # Although I acknowledge that friday might now be the last trading day due to holidays
    datetimeDate = datetime.strptime(dateString+'  1:33PM', '%Y-%m-%d %I:%M%p').date()
    return datetimeDate





def percentChangesByDayScaled(stock_close_ordered_dict, scaleInterval):
    instagramFoundDate = datetime(2010, 10, 6).date()

    print("starting: percentChangesByDayScaled(nasdaqDataDaily, 'weekly)")
    scaleByThisSeries = pullStockPriceHistoryData(av_key, retailerNasdaq, series=scaleInterval)
    print(" okay let me see what dates are in the weekly series")
    print(scaleByThisSeries)
    listPrices = []
    dates = []
    stockMetrics = dict()
    count1 = 0
    count2 = 0


    print("Stock Price, Date")
    for key in stock_close_ordered_dict:
        if stringToDatetimeDate(key) > instagramFoundDate:
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
        inputIsoWeek = stringToDatetimeDate(dates[i]).isocalendar()[1]
        inputIsoYear = stringToDatetimeDate(dates[i]).isocalendar()[0]
        todayIsoWeek = datetime.today().isocalendar()[1]
        todayIsoYear = datetime.today().isocalendar()[0]
        inputDayAsDatetime = stringToDatetimeDate(dates[i])

        count2 += 1
        percent_comparison = (listPrices[i]-avgPrice)/avgPrice * 100
        list_comparisons.append(percent_comparison)
        roundedToFriday = roundToLastTradingDay(roundToNearestFriday(dates[i]))
        # print(roundToLastTradingDay(roundedToFriday))
        # First if condition, dates in the same week as today (and today isn't friday yet) will raise an error
        # print(scaleByThisSeries)
        # what happens when we hit monday of this week, error, let's fix it
        # if the weekday is less than today. So last week's friday is 4
        # today is monday and that's 0
        # Friday won't raise an exception with the following if condition
        if inputIsoWeek == todayIsoWeek and inputIsoYear == todayIsoYear and inputDayAsDatetime > instagramFoundDate:
            weeklyAvg = scaleByThisSeries[str(datetime.today().date())]
        else:
            if str(roundedToFriday) == '2011-04-22':
                weeklyAvg =  scaleByThisSeries[str(roundedToFriday-timedelta(1))]
            elif str(roundedToFriday) == '2011-11-10':
                weeklyAvg =  scaleByThisSeries[str(roundedToFriday+timedelta(1))]
            else:
                weeklyAvg = scaleByThisSeries[str(roundedToFriday)]
            if stringToDatetimeDate(dates[i]).weekday() < datetime.today().weekday():
                stringToDatetimeDate(dates[i]).isocalendar()[1] = datetime.today().isocalendar()[1]
                print(stringToDatetimeDate(dates[i]))
                print(datetime.today().isocalendar()[1])


                pass

                if count2 < 5:
                    print(percent_comparison, 0)
                    print("date again: ", dates[i])
                    print("Let's try rounding this to the nearest end of week trading day (Friday if non-holiday)")
                    print("lets check if our round to friday returns a stock data point below")
                    print(scaleByThisSeries[str(roundedToFriday)], type(scaleByThisSeries[str(roundedToFriday)]))
                    print("Percent Comparison to Weekly Avg: ", percentComparisonToInterval)
                # print(scaleByThisSeries[roundedToFriday])

    percentComparisonToInterval = (listPrices[i] - weeklyAvg) / weeklyAvg * 100
    listIntervalComparisons.append(percentComparisonToInterval)
    stockMetrics["prices"] = listPrices
    stockMetrics["price_percent_changes"] = list_comparisons
    stockMetrics["price_percent_changes_"+scaleInterval] = list_comparisons

    stockMetrics["date_strings"] = dates
    return stockMetrics




# for key in stock_close_ordered_dict:
    # print(stock_close_ordered_dict[key])