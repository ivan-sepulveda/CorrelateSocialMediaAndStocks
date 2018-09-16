# from comparison import *
from pullSocialMediaPresence import *
from SocialMediaAnalysis import *
from pullStockPriceHistory import *
from stockAnalysis import *
from plotSocialMediaVsStocks import *

# Now we'll pick a retailer by inputting both their IG handle and
retailerIg = "adidas"
# Now let's enter the same retailers NASDAQ index
retailerNasdaq = "ADDYY"
# alpha_vantage key
av_key = "HQXQHIFN548EZELL"

# Step 1: If we haven't already downloaded our retailers IG-like-history into a directory we'll scrape it now.
if not doesJsonExist(retailerIg):
    webscrapeJson(retailerIg)
# Step 2: Now we have to parse this json file and run analytics.
filteredJson_ = filteredDecodedJson(retailerIg)
metrics_ = returnMetricsListsDict(filteredJson_)
socialMediaMetrics = addAveragesToMetrics(metrics_, filteredJson_)
# Step 3: Lets pull our NASDAQ data
nasdaqData = pullStockPriceHistoryData(av_key, retailerNasdaq)
# Step 4: Parse through data and run analytics
stockPriceMetrics = returnPercentChangesByDate(nasdaqData)
# Step 5: Plot both metrics against each other
print(socialMediaMetrics.keys())
stockSeries = convertToPandaSeries(stockPriceMetrics["price_percent_changes"], stockPriceMetrics["date_strings"])
mediaSeries = convertToPandaSeries(socialMediaMetrics["likes_percent_changes"], socialMediaMetrics["timestamps"])
plotSocialMediaVsStocks(mediaSeries, stockSeries)







# # first lemme compare the date range
# print("stocks")
# print(stockPriceMetrics["date_strings"])
# print("social media")
# print(socialMediaMetrics["timestamps"])



