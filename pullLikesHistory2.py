from instagram_scraper import app
import os
import json


# scrp_accnt = "nike"
# login_u = "appleseedjohn506"
# login_p = "e3e-y5V-HSt-RN9"
# mx_ = "3"
# os.system("instagram-scraper {0} -u {1} -p {2} -m {3} -t none --media-metadata".format(scrp_accnt,login_u,login_p, mx_))
# Now we are going to try and obtain the json file

os.chdir(os.getcwd()+"/"+scrp_accnt)
input_file = open(scrp_accnt+'.json', 'r')
json_decode = json.load(input_file)
os.chdir(home_directory)


def returnJsonFile(retailerIG):
    os.chdir(os.getcwd() + "/" + scrp_accnt)
    input_file = open(scrp_accnt + '.json', 'r')
    json_decode = json.load(input_file)
    os.chdir(home_directory)


def go_time2():
    home_directory = os.getcwd()
    scrp_accnt = "nike"
    os.chdir(os.getcwd() + "/" + scrp_accnt)
    input_file = open(scrp_accnt + '.json', 'r')
    json_decode = json.load(input_file)
    # print("below is json decode from json.load(input_file)")
    # print(json_decode)
    # metrics = json_decode['entry_data']
    # print(metrics)

    # metrics = json_decode['entry_data']['ProfilePage'][0]['graphql']['user']
    os.chdir(home_directory)
    return json_decode