from stockAnalysis import *
from SocialMediaAnalysis import *
import matplotlib.dates as mdates
import numpy as np

# Plotting all the stock data
dates2 = []
for d in dates:
    dates2.append(convert_str_to_date(d))

s = pd.Series(list_comparisons, index=dates2)

fig, ax = plt.subplots()
ax.plot(s.index, s.values, label="Closing Stock Price")


datemin = np.datetime64(dates2[0], 'D')
datemax = np.datetime64(dates2[-1], 'D') + np.timedelta64(1, 'D')
ax.set_xlim(datemin, datemax)

print("datemin")
print(datemin)
print(type(datemin))


ax.xaxis.set_minor_locator(mdates.DayLocator())
monthDayFrmt = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(monthDayFrmt)

# Plotting all the Instagram data
print("listOfTimeStamps")
print(listOfTimeStamps, len(listOfTimeStamps))
print("all_like_comps")
print(all_like_comps, len(all_like_comps))


y2 = np.cumsum(np.random.normal(size=len(listOfTimeStamps)))
modified_likeComps = np.asarray(all_like_comps)/15
s2 = pd.Series(modified_likeComps, index=listOfTimeStamps)

# ax.plot()
ax.plot(s2.index, s2.values, label="Instagram Likes")
#
# datemin = np.datetime64(post_timeline_days[0], 'D')
# datemax = np.datetime64(post_timeline_days[-1], 'D') + np.timedelta64(1, 'D')
# ax.set_xlim(datemin, datemax)
#
# ax.xaxis.set_minor_locator(mdates.DayLocator())
# monthDayFrmt = mdates.DateFormatter("%m/%d")
# ax.xaxis.set_major_formatter(monthDayFrmt)


# Final Plot
plt.ylabel("% Increase/Decrease from Avg")
plt.legend()
fig.savefig("Social Media Comparison.png")
plt.show()
# plt.ax.savefig("Social Media Comparison.png")
# plt.savefig("trial.pdf")
