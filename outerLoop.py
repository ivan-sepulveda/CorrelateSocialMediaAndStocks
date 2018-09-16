# from comparison import *
import os



# Let's set our home directory we we always know where to revert back to
homeDirectory = os.getcwd()
# Now we'll pick a retailer by inputting both their IG handle and
retailerIg = "nike"
# Now let's enter the same retailers NASDAQ index
retailerNasdaq = "NKE"

# Step 1: Let's check if we've already downloaded our retailers IG like history into a directory
# If it does exist, we can go ahead and parse it, calculate avg like/comment volume, list deviations, etc.
if os.path.isdir(homeDirectory+"/"+retailerIg):
    print("Directory {0} exists. Checking for .json file.".format(retailerIg))
    if os.path.exists(homeDirectory+"/"+retailerIg+"/"+retailerIg+".json"):
        print("{0}.json file exists".format(retailerIg))
# If not, we'll create it before proceeding.
else:

    pass

