# # Probably need instagram API
# from InstagramAPI import InstagramAPI
# from get_all_comments import get_those_comments
#
# url_piece = "BnAEUiAnBv9"
#
def media_id_to_code(media_id):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    short_code = ''
    while media_id > 0:
        remainder = media_id % 64
        media_id = (media_id-remainder)/64
        short_code = alphabet[remainder] + short_code
    return short_code


def code_to_media_id(short_code):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    media_id = 0;
    for letter in short_code:
        media_id = (media_id*64) + alphabet.index(letter)

    return media_id

print(code_to_media_id("BkUWGRcnaXZ"))

#
#
# print(code_to_media_id(url_piece))
# get_those_comments(str(code_to_media_id(url_piece)))


# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# #
# # Use text editor to edit the script and type in valid Instagram username/password
#
# from InstagramAPI import InstagramAPI as IAPI1
# import time
# from datetime import datetime
#
# temp_media_id = '1477006830906870775_19343908'
#
# # stop conditions, the script will end when first of them will be true
# until_date = '2017-03-31'
# count = 100
#
# API = IAPI1("sepulverizer_", "fucksocialmedia1!")
#
# API.login()
# uid = 192495483
# # uida = API.getUsernameInfo(API.username_id)
# comments = []
#
# def get_those_comments(media_id):
#     has_more_comments = True
#     max_id = ''
#     while has_more_comments:
#         _ = API.getMediaComments(media_id, max_id=max_id)
#         # comments' page come from older to newer, lets preserve desc order in full list
#         for c in reversed(API.LastJson['comments']):
#             comments.append(c)
#         has_more_comments = API.LastJson.get('has_more_comments', False)
#         # evaluate stop conditions
#         if count and len(comments) >= count:
#             comments = comments[:count]
#             # stop loop
#             has_more_comments = False
#             print("stopped by count")
#         if until_date:
#             older_comment = comments[-1]
#             dt = datetime.utcfromtimestamp(older_comment.get('created_at_utc', 0))
#             # only check all records if the last is older than stop condition
#             if dt.isoformat() <= until_date:
#                 # keep comments after until_date
#                 comments = [
#                     c
#                     for c in comments
#                     if datetime.utcfromtimestamp(c.get('created_at_utc', 0)) > until_date
#                 ]
#                 # stop loop
#                 has_more_comments = False
#                 print("stopped by until_date")
#         # next page
#         if has_more_comments:
#             max_id = API.LastJson.get('next_max_id', '')
#             time.sleep(2)

# aa = "https://scontent-sjc3-1.cdninstagram.com/vp/00f1780c6795660b0ec4d88f8a7a4cdf/5B978F54/t51.2885-15/e15/c0.90.720.720/s150x150/35000948_425788114554343_2999169383554613248_n.jpg"