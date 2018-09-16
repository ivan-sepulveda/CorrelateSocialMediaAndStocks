from statistics import mean
# from pullLikesHistory import InstagramScraper
import dateutil.parser
from pullLikesHistory2 import go_time2
from datetime import datetime


# temporarily commenting next 2 lines out, trying out PullLikesHistory2
# k = InstagramScraper()
# postsDictionary = k.profile_page_recent_posts('https://www.instagram.com/nike/?hl=en')

# PullLikes History 2
# k = InstagramScraper()

metrics = go_time2()
# print(postsDictionary)


listOfLikes = list()
listOfComments = list()
listOfTimeStamps = list()
all_like_comps = list()
all_comment_comps = list()


for node in metrics:
    print(type(node))
    if len(node) > 0:
        unixTimestamp = node["taken_at_timestamp"]
        listOfTimeStamps.append(datetime.utcfromtimestamp(unixTimestamp).strftime('%Y-%m-%d'))
        # listOfTimeStamps.append(node["taken_at_timestamp"])
        listOfComments.append(node["edge_media_to_comment"]["count"])
        listOfLikes.append(node["edge_media_preview_like"]["count"])
        # listOfTimeStamps.append(dateutil.parser.parse(node["taken_at_timestamp"]))

        print(node)
        for key in node:
            print(key)
    # print(node["edge_liked_by"]['count'])
    # listOfLikes.append(post["like_count"])
    # listOfComments.append(post["comment_count"])
    # listOfTimeStamps.append(dateutil.parser.parse(post["uploaded"]))



print(listOfLikes)
print(listOfComments)
print(listOfTimeStamps)

avg_likes = mean(listOfLikes)
avg_comments = mean(listOfComments)
print("avg_likes", avg_likes)
print("avg_comments", avg_comments)


for post in metrics:
    post["comparison_to_avg_likes"] = (avg_likes - post["edge_media_preview_like"]["count"])/avg_likes * 100
    post["comparison_to_avg_comments"] = (avg_comments - post["edge_media_to_comment"]["count"])/avg_comments * 100


print("first post at: ", listOfTimeStamps[0])
print("last post at:", listOfTimeStamps[-1])

# print("Time difference = ", '{0: 4g}'.format(listOfTimeStamps[-1]-listOfTimeStamps[0]))
# print(listOfTimeStamps[0]-listOfTimeStamps[1])
# print(post_timeline_days)

for node in metrics:
#     listOfLikes.append(post["like_count"])
#     listOfComments.append(post["comment_count"])
#     listOfTimeStamps.append(dateutil.parser.parse(post["uploaded"]))
    all_like_comps.append(node["comparison_to_avg_likes"])
    all_comment_comps.append(node["comparison_to_avg_comments"])

start = datetime.strptime(listOfTimeStamps[0], '%Y-%m-%d')
print(start)
print(type(start))
# post_timeline_days = (listOfTimeStamps[0]-listOfTimeStamps[1]).days
