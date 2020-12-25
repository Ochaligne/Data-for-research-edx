import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature

birddata = pd.read_csv("bird_tracking.csv")
#print(birddata.info())
#print(birddata.head())
bird_names = pd.unique(birddata.bird_name)
#print(bird_names)
"""
plt.figure(figsize=(7,7))
for bird_name in bird_names:
    iloc = birddata.bird_name == bird_name
    x , y = birddata.longitude[iloc], birddata.latitude[iloc]
    plt.plot(x,y,".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("migration.pdf")
"""
"""
#Plotting using pyplot
plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency");
#plt.savefig("hist.pdf")
plt.show()

#Plotting using pandas (Takes care of NaN values)
birddata.speed_2d.plot(kind='hist', range=[0,30])
plt.xlabel("2D Speed")
plt.savefig("pd_hist.pdf")

#count and check non available numbers
print(np.sum(np.isnan(speed)))
"""
"""
#delta time
time_1 = datetime.datetime.today()

time_2 = datetime.datetime.today()
print(time_2 - time_1)
"""

date_str = birddata.date_time[0]
#print(date_str)
#Convert to datetime object
datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

#Storing converted time stamps
timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamps"] = pd.Series(timestamps, index = birddata.index)

times = birddata.timestamps[birddata.bird_name == "Sanne"]
#elapsed_time = [time - times[0] for time in times]
print(timestamps[0:3])
#print(birddata.timestamps[4] - birddata.timestamps[3])
#print(birddata.head())
#print(elapsed_time[1000])
#Calculating days
#print(elapsed_time[1000]/ datetime.timedelta(days=1)) #hours=1
"""
#Plotting
plt.plot(np.array(elapsed_time)/ datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time (days)");
plt.savefig("timeplot.pdf")

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamps
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i,t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        #compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []
#Plotting
plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)");
plt.savefig("dms.pdf")
"""

proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

for name in bird_names:
    iloc = birddata['bird_name'] == name
    x , y = birddata.longitude[iloc], birddata.latitude[iloc]
    ax.plot(x,y,".", transform=ccrs.Geodetic(), label=name)

plt.legend(loc="upper left")
plt.savefig("map.pdf")
