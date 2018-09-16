import os
import json
# Let's set our home directory we we always know where to revert back to

def doesJsonExist(retailerIg):
    homeDirectory = os.getcwd()
    if os.path.isdir(homeDirectory+"/"+retailerIg):
        if os.path.exists(homeDirectory+"/"+retailerIg+"/"+retailerIg+".json"):
            print("{0}.json file exists".format(retailerIg))
            return True

def webscrapeJson(retailerIg):
    print("Web-scraping @{0}, creating json.file".format(retailerIg))
    login_u = "appleseedjohn506"
    login_p = "e3e-y5V-HSt-RN9"
    os.system("instagram-scraper {0} -u {1} -p {2} -t none --media-metadata".format(retailerIg, login_u, login_p))
    print("Web-scraping complete.")

def returnDecodedJson(retailerIg):
    homeDirectory = os.getcwd()
    os.chdir(homeDirectory + "/" + retailerIg)
    input_file = open(retailerIg + '.json', 'r')
    json_decode = json.load(input_file)
    os.chdir(homeDirectory)
    return json_decode