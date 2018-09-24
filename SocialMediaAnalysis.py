from statistics import mean
import dateutil.parser
from datetime import datetime
from pullSocialMediaPresence import returnDecodedJson
import pullUserVolumeStats as uvs
from initialConditions import *



def filteredDecodedJson(retailerIg_, keepDateAsUnix = False):
    decodedJson = returnDecodedJson(retailerIg_)
    filtered = dict()
    for node_ in decodedJson:
        if len(decodedJson) > 0:
            unixTimestamp = node_["taken_at_timestamp"]
            filtered[unixTimestamp] = dict()
            filtered[unixTimestamp]["comment_volume"] = node_["edge_media_to_comment"]["count"]
            filtered[unixTimestamp]["like_volume"] = node_["edge_media_preview_like"]["count"]
            if keepDateAsUnix:
                filtered[unixTimestamp]["date_string"] = unixTimestamp
                pass
            else:
                filtered[unixTimestamp]["date_string"] = datetime.utcfromtimestamp(unixTimestamp).strftime('%Y-%m-%d')

    return filtered


def returnMetricsListsDict(filteredJson):
    listLikesVolume = list()
    listCommentsVolume = list()
    listTimeStampStrings = list()
    for elem in filteredJson:
        listLikesVolume.append(filteredJson[elem]["like_volume"])
        listCommentsVolume.append(filteredJson[elem]["comment_volume"])
        listTimeStampStrings.append(filteredJson[elem]["date_string"])
    metrics_ = dict()
    metrics_["likes"] = listLikesVolume
    metrics_["comments"] = listCommentsVolume
    metrics_["timestamps"] = listTimeStampStrings
    return metrics_


def addAveragesToMetrics(regularMetrics, filteredJson):
    updatedMetrics = dict(regularMetrics.copy())
    listLikeChangePercentages = list()
    listCommentChangePercentages = list()

    avg_likes = mean(regularMetrics["likes"])
    avg_comments = mean(regularMetrics["comments"])
    for post in filteredJson:
        listLikeChangePercentages.append(100*(filteredJson[post]["like_volume"] - avg_likes)/avg_likes)
        listCommentChangePercentages.append(100*(filteredJson[post]["comment_volume"] - avg_comments)/avg_comments)
    updatedMetrics["likes_percent_changes"]= listLikeChangePercentages
    updatedMetrics["comments_percent_changes"]= listCommentChangePercentages
    updatedMetrics["timestamps"]= regularMetrics["timestamps"]

    return updatedMetrics



def userScaledMetrics(lksPrcntChngs, dateTimeStampsIG, dateTimesFromUserDict):
    userScaledMetricsDct = dict()
    userScaledMetricsDct["scaledLikesPercentChanges"] = list()
    userScaledMetricsDct["scaledCommentsPercentChanges"] = list()
    userScaledMetricsDct["timestamps"] = dateTimeStampsIG[:]
    count = 0
    # print(len(lksPrcntChngs), len(dateTimeStampsIG))
    today = datetime.now()
    for i in range(len(dateTimeStampsIG)):
        count += 1
        usersAfterJune18 = 1000000000
        percentChangeForPost = lksPrcntChngs[i]
        postDate = dateTimeStampsIG[i]
        postDay = postDate.day
        postMonth = postDate.month
        postYear = postDate.year
        if datetime(postYear, postMonth, postDay) < today:
            # assuming 1 billion users
            scaleFactor = 1/(usersAfterJune18/10000000)
            scaledPercentChange = percentChangeForPost*scaleFactor
        else:
            usersOnThisDate = dateTimesFromUserDict[postDate]
            scaleFactor = 1/(usersOnThisDate/10000000)

            scaledPercentChange = percentChangeForPost*scaleFactor
        userScaledMetricsDct["scaledLikesPercentChanges"].append(scaledPercentChange)
        # print(i, "postdate", dateTimeStampsIG[i], scaledPercentChange)

    # print(userScaledMetricsDct["scaledLikesPercentChanges"])
    return userScaledMetricsDct



filteredJson1 = filteredDecodedJson(retailerIg, keepDateAsUnix=True)
baseMetrics = returnMetricsListsDict(filteredJson1)
comparisonMetrics = addAveragesToMetrics(baseMetrics, filteredJson1)
# print("comparisonMetrics[timestamps])")

def stringDatesToDatetimeDates(retailerComparisonMetrics):

    return [uvs.convert_str_to_date_notime(uvs.timestampToStr(e)) for e in retailerComparisonMetrics["timestamps"]]

IG_TS_as_DT = [uvs.convert_str_to_date_notime(uvs.timestampToStr(e)) for e in comparisonMetrics["timestamps"]]
# print(IG_TS_as_DT)
# keyVariable = comparisonMetrics["timestamps"][0]
# keyAsString = uvs.timestampToStr(keyVariable)

# userScaledMetrics(comparisonMetrics["likes_percent_changes"], IG_TS_as_DT, uvs.dateValueDict)

# a = datetime.date(2018, 9, 15, 0 , 0, 0)
# for t in uvs.dateValueDict:
#     print(type(t))
#     break
#
# t = datetime.date(datetime(2012, 9, 15))
# print(uvs.dateValueDict[t])