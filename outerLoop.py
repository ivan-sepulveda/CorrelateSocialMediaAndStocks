# from comparison import *
from pullSocialMediaPresence import *
from pullStockPriceHistory import *
from stockAnalysis import *
import pullUserVolumeStats as puvs
from initialConditions import *



# Step 1: If we haven't already downloaded our retailers IG-like-history into a directory we'll scrape it now.
if not doesJsonExist(retailerIg):
    webscrapeJson(retailerIg)
from SocialMediaAnalysis import *
from plotSocialMediaVsStocks import *


# Step 2: Now we have to parse this json file and run analytics.
filteredJson_ = filteredDecodedJson(retailerIg)
metrics_ = returnMetricsListsDict(filteredJson_)
socialMediaMetrics = addAveragesToMetrics(metrics_, filteredJson_)
abc = puvs.dateValueDict
igTimestampsAsDates = stringDatesToDatetimeDates(socialMediaMetrics)
scaledMetrics = userScaledMetrics(socialMediaMetrics["likes_percent_changes"], igTimestampsAsDates, abc)
# Step 3: Lets pull our NASDAQ data
nasdaqDataDaily = pullStockPriceHistoryData(av_key, retailerNasdaq)
# nasdaqDataWeekly = pullStockPriceHistoryData(av_key, retailerNasdaq, series="weekly")
# print(nasdaqDataWeekly)


# Step 4: Parse through data and run analytics
stockPriceMetrics = returnPercentChangesByDate(nasdaqDataDaily)
# Step 5: Plot both metrics against each other
stockSeries = convertToPandaSeries(stockPriceMetrics["price_percent_changes"], stockPriceMetrics["date_strings"])
mediaSeries = convertToPandaSeries(socialMediaMetrics["likes_percent_changes"], socialMediaMetrics["timestamps"])
# Step 5.5: Overlap dates
relevantNasdaqSeries = overlapSeriesDates(mediaSeries, stockSeries)
print("relevant nasdaq")
print(relevantNasdaqSeries)
#
plotSocialMediaVsStocks(mediaSeries, relevantNasdaqSeries, retailerIg)

# Step 6: Plot dynamically user scaled version. Using the same stock series
scaledMediaMetricsSeries = convertToPandaSeries(scaledMetrics["scaledLikesPercentChanges"], socialMediaMetrics["timestamps"])
scaledMediaSeries = convertToPandaSeries(scaledMediaMetricsSeries, socialMediaMetrics["timestamps"])
plotUserScaledSocialMediaVsStocks(scaledMediaMetricsSeries, relevantNasdaqSeries, retailerIg)
# #
# #
#
#
#
