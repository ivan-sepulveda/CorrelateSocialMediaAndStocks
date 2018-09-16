from statistics import mean
# from pullLikesHistory import InstagramScraper
import dateutil.parser
# from pullLikesHistory2 import go_time2
from datetime import datetime
from pullSocialMediaPresence import returnDecodedJson



def filteredDecodedJson(retailerIg_):
    decodedJson = returnDecodedJson(retailerIg_)
    filtered = dict()
    for node_ in decodedJson:
        if len(decodedJson) > 0:
            unixTimestamp = node_["taken_at_timestamp"]
            filtered[unixTimestamp] = dict()
            filtered[unixTimestamp]["comment_volume"] = node_["edge_media_to_comment"]["count"]
            filtered[unixTimestamp]["like_volume"] = node_["edge_media_preview_like"]["count"]
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
    return updatedMetrics



    # for node in decodedJson:
    #     print(node)
    #     print(type(node))
    #     if len(node) > 0:
    #         unixTimestamp = node["taken_at_timestamp"]
    #         listOfTimeStamps.append(datetime.utcfromtimestamp(unixTimestamp).strftime('%Y-%m-%d'))
    #         listOfComments.append(node["edge_media_to_comment"]["count"])
    #         listOfLikes.append(node["edge_media_preview_like"]["count"])
    #         print(node)
    #         for key in node:
    #             print(key)
    #
    # print(listOfLikes)
    # print(listOfComments)
    # print(listOfTimeStamps)
    #
    # avg_likes = mean(listOfLikes)
    # avg_comments = mean(listOfComments)
    # print("avg_likes", avg_likes)
    # print("avg_comments", avg_comments)
    #
    # for post in decodedJson:
    #     post["comparison_to_avg_likes"] = (avg_likes - post["edge_media_preview_like"]["count"]) / avg_likes * 100
    #     post["comparison_to_avg_comments"] = (avg_comments - post["edge_media_to_comment"][
    #         "count"]) / avg_comments * 100
    #
    # print("first post at: ", listOfTimeStamps[0])
    # print("last post at:", listOfTimeStamps[-1])
    #
    # for node in decodedJson:
    #     all_like_comps.append(node["comparison_to_avg_likes"])
    #     all_comment_comps.append(node["comparison_to_avg_comments"])
    # return





















# def returnMetricsListsDict(cleanedUpJson):
#     decodedJson = returnDecodedJson(retailerIg_)
#     listOfLikes = list()
#     listOfComments = list()
#     listOfTimeStamps = list()
#     all_like_comps = list()
#     all_comment_comps = list()
#     return e



# metrics = go_time2()
#
# listOfLikes = list()
# listOfComments = list()
# listOfTimeStamps = list()
# all_like_comps = list()
# all_comment_comps = list()


# for node in metrics:
#     print(type(node))
#     if len(node) > 0:
#         unixTimestamp = node["taken_at_timestamp"]
#         listOfTimeStamps.append(datetime.utcfromtimestamp(unixTimestamp).strftime('%Y-%m-%d'))
#         listOfComments.append(node["edge_media_to_comment"]["count"])
#         listOfLikes.append(node["edge_media_preview_like"]["count"])
#         print(node)
#         for key in node:
#             print(key)
#
#
# print(listOfLikes)
# print(listOfComments)
# print(listOfTimeStamps)
#
# avg_likes = mean(listOfLikes)
# avg_comments = mean(listOfComments)
# print("avg_likes", avg_likes)
# print("avg_comments", avg_comments)
#
#
# for post in metrics:
#     post["comparison_to_avg_likes"] = (avg_likes - post["edge_media_preview_like"]["count"])/avg_likes * 100
#     post["comparison_to_avg_comments"] = (avg_comments - post["edge_media_to_comment"]["count"])/avg_comments * 100
#
#
# print("first post at: ", listOfTimeStamps[0])
# print("last post at:", listOfTimeStamps[-1])
#
# for node in metrics:
#     all_like_comps.append(node["comparison_to_avg_likes"])
#     all_comment_comps.append(node["comparison_to_avg_comments"])
#
# start = datetime.strptime(listOfTimeStamps[0], '%Y-%m-%d')
# print(start)
# print(type(start))
