from stockAnalysis import *
from SocialMediaAnalysis import *
import matplotlib.dates as mdates
from matplotlib.dates import MONDAY
import numpy as np
from pullStockPriceHistory import convert_str_to_date
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter




def reformatDatesList(listDatesAsStrings):
    datetime_dates = []
    for d in listDatesAsStrings:
        datetime_dates.append(convert_str_to_date(d))
    return datetime_dates
# Plotting all the stock data


def convertToPandaSeries(listIncreasesDecreases, listDatesAsStrings):
    return pd.Series(listIncreasesDecreases, index=reformatDatesList(listDatesAsStrings))

def overlapSeriesDates(socialPandaSeries, stockPandaSeries):
    # will come back to this
    reducedStockSeries = stockPandaSeries.copy()
    print("starting overlapSeriesDates")
    firstIgPost = min(socialPandaSeries.index)
    print(type(firstIgPost))
    print("first ig post: ", firstIgPost)
    print("these are before that")
    lastRelevantDateIdex = 0
    for i in range(len(reducedStockSeries.index)):
        if reducedStockSeries.index[i] <= firstIgPost:
            lastRelevantDateIdex = i
            # listToDrop.append(reducedStockSeries.index[i])
            # reducedStockSeries = reducedStockSeries[i:]
            # reducedStockSeries.drop(reducedStockSeries.index[i])
            # print(reducedStockSeries.index.size)

    # reducedStockSeries.drop(labels=listToDrop)
    # print(reducedStockSeries)
    return reducedStockSeries[lastRelevantDateIdex:]

def plotSocialMediaVsStocks(socialPandaSeries, stockPandaSeries, company, formatBy = "M", interval=1):
    fig, ax = plt.subplots()
    datemin_social = np.datetime64(socialPandaSeries.index[0], formatBy)
    datemax_social = np.datetime64(socialPandaSeries.index[-1], formatBy) + np.timedelta64(1, formatBy)
    datemin_stocks = np.datetime64(stockPandaSeries.index[0], formatBy)
    datemax_stocks = np.datetime64(stockPandaSeries.index[-1], formatBy) + np.timedelta64(1, formatBy)
    # First let's check and make sure that social timeseries data didn't get spit out in the wrong order
    if datemax_social < datemin_social:
        datemin_social, datemax_social = datemax_social, datemin_social
    # Same thing for stock timeseries
    if datemax_stocks < datemin_stocks:
        datemin_stocks, datemax_social = datemax_social, datemin_stocks
    # Now let's overlap
    overallMin = datemin_social
    overallMax = datemax_social
    # let's say the social media first give post was January, but the first stock data
    # was March. We'd want the March date as our minimum
    if overallMin < datemin_stocks:
        overallMin = datemin_stocks
    # let's say the social media last post was in July. And last stock data was September. We'd want July
    # let's say the social media last post was in September. And last stock data was July
    # We'd want July again so we'd get the last stock price
    if datemax_stocks < overallMin:
        overallMax = datemax_stocks
    ax.set_xlim(overallMin, overallMax)

    # every monday
    mondays = WeekdayLocator(MONDAY)

    # every month
    months = MonthLocator(range(1, 13), bymonthday=1, interval=interval)
    monthsFmt = DateFormatter("%b '%y")

    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(monthsFmt)
    ax.xaxis.set_minor_locator(mondays)
    fig.autofmt_xdate()
    ax.plot(stockPandaSeries.index, stockPandaSeries.values, label="Closing Stock Price")
    ax.plot(socialPandaSeries.index, socialPandaSeries.values, label="Social Media Presence")
    # Final Plot
    plt.ylabel("% Increase/Decrease from Avg")
    plt.title(company)
    plt.legend()
    fig.savefig("Social Media Comparison.png")
    plt.show()

def plotUserScaledSocialMediaVsStocks(socialPandaSeries, stockPandaSeries, company, formatBy = "M", interval=1):
    fig, ax = plt.subplots()
    datemin_social = np.datetime64(socialPandaSeries.index[0], formatBy)
    datemax_social = np.datetime64(socialPandaSeries.index[-1], formatBy) + np.timedelta64(1, formatBy)
    datemin_stocks = np.datetime64(stockPandaSeries.index[0], formatBy)
    datemax_stocks = np.datetime64(stockPandaSeries.index[-1], formatBy) + np.timedelta64(1, formatBy)
    # First let's check and make sure that social timeseries data didn't get spit out in the wrong order
    if datemax_social < datemin_social:
        datemin_social, datemax_social = datemax_social, datemin_social
    # Same thing for stock timeseries
    if datemax_stocks < datemin_stocks:
        datemin_stocks, datemax_social = datemax_social, datemin_stocks
    # Now let's overlap
    overallMin = datemin_social
    overallMax = datemax_social
    # let's say the social media first give post was January, but the first stock data
    # was March. We'd want the March date as our minimum
    if overallMin < datemin_stocks:
        overallMin = datemin_stocks
    # let's say the social media last post was in July. And last stock data was September. We'd want July
    # let's say the social media last post was in September. And last stock data was July
    # We'd want July again so we'd get the last stock price
    if datemax_stocks < overallMin:
        overallMax = datemax_stocks
    ax.set_xlim(overallMin, overallMax)
    # every monday
    mondays = WeekdayLocator(MONDAY)

    # every month
    months = MonthLocator(range(1, 13), bymonthday=1, interval=interval)
    monthsFmt = DateFormatter("%m/%y")

    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(monthsFmt)
    ax.xaxis.set_minor_locator(mondays)
    fig.autofmt_xdate()
    ax.plot(stockPandaSeries.index, stockPandaSeries.values, label="Closing Stock Price")
    ax.plot(socialPandaSeries.index, socialPandaSeries.values, label="Social Media Presence")
    # Final Plot
    plt.ylabel("Scaled % Increase/Decrease from Avg")
    plt.title(company)
    plt.legend()
    fig.savefig("Scaled Social Media Comparison.png")
    plt.show()

