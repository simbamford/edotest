# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 15:46:34 2023

@author: sbamford
"""


import os, sys
prefix = 'C:/' if os.name == 'nt' else '/home/sbamford/'
sys.path.insert(0, os.path.join(prefix, 'repos')) # for mustard
sys.path.insert(0, os.path.join(prefix, 'repos/Sim'))
#sys.path.insert(0, os.path.join(prefix, 'repos/bimvee-iityarpextensions')) # prepend to override installed package
sys.path.insert(0, os.path.join(prefix, 'repos/bimvee')) # prepend to override installed package

#%%


from bimvee.importAe import importAe

filePathOrName =  "C:/data/2023-08-29-14-44-22.bin"
filePathOrName =  "C:/data/2023-09-01-16-12-25.bin"
container = importAe(filePathOrName=filePathOrName)

#%%

from bimvee.plot import plot

plot(container)

#%%


from bimvee.plotEventRate import plotEventRate

plotEventRate(container, periods=[0.1])

#%%

from bimvee.plotDvsContrast import plotDvsContrast

plotDvsContrast(container, numPlots=2)

#%%

import numpy as np

data = container['data']['ch0']['dvs']

x = data['x']
y = data['y']
ts = data['ts']

timeStart = 2.5
timeEnd = 3.5

timeStartIdx = np.argmax(ts > timeStart)
timeEndIdx = np.argmax(ts > timeEnd)

import matplotlib.pyplot as plt

plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x[timeStart:timeEnd],
           y[timeStart:timeEnd],
           ts[timeStart:timeEnd],
           marker='o',
           s = 1)

#%%

timeStart = 2.8
timeEnd = 3.0


xStart = 50
xEnd = 150

yStart = 200
yEnd = 300


keep = x > xStart 
print(np.sum(keep))

keep = np.logical_and(keep, x < xEnd)
print(np.sum(keep))

keep = np.logical_and(keep, y > yStart)
print(np.sum(keep))

keep = np.logical_and(keep, y < yEnd)
print(np.sum(keep))

keep = np.logical_and(keep, ts > timeStart)
print(np.sum(keep))

keep = np.logical_and(keep, ts < timeEnd)
print(np.sum(keep))

xKept = x[keep]
yKept = y[keep]
tsKept = ts[keep]

import matplotlib.pyplot as plt

plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(xKept,
           yKept,
           tsKept,
           marker='o',
           s = 1)




#%%

timeStart = 2.5
timeEnd = 3.5

from bimvee.split import cropSpaceTime

kept = cropSpaceTime(data, 
                     minX=xStart, maxX=xEnd,
                     minY=yStart, maxY=yEnd,
                     minTime=timeStart, maxTime=timeEnd,
                     zeroSpace=True)

plotDvsContrast(kept)

#%%
from bimvee.plotEventRate import plotEventRate

plotEventRate(kept, periods=[0.01])

#%%

from bimvee.plotSpikeogram import plotSpikeogram

kept['addr'] = kept['x'] * 100 + kept['y']
plotSpikeogram(kept)

#%%
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(kept['x'],
           kept['y'],
           kept['ts'],
           marker='o',
           s = 1)


#%% start visualiser

import threading

# Start a visualizer
import mustard.mustard
app = mustard.mustard.Mustard()
thread = threading.Thread(target=app.run)
thread.daemon = True
thread.start()

print(mustard.__file__)

#%%
app.setData(container)

#%%
data = container['data']['ch0']['dvs']

timeStart = 4.2
timeEnd = 4.25

from bimvee.split import cropSpaceTime
from bimvee.plotDvsContrast import plotDvsContrast

kept = cropSpaceTime(data, 
                     minTime=timeStart, maxTime=timeEnd,
                     zeroSpace=True)

plotDvsContrast(kept, numPlots=1, proportionOfPixels = 1.0)

#%%
import numpy as np

data = container['data']['ch0']['dvs']
ts = data['ts']

uniqueTs = np.unique(ts)

import matplotlib.pyplot as plt

plt.plot(uniqueTs, np.ones_like(uniqueTs), 'o')

#%%

from bimvee.split import cropTime

kept = cropTime(data, 
                minTime=4.38, maxTime=4.39,
                zeroTime=False)

plt.plot(kept['ts'], kept['y'] * 640 + kept['x'], 'o')


#%%
from bimvee.plotEventRate import plotEventRate



plotEventRate(data, periods=[0.001])

#%%
import numpy as np

data = container['data']['ch0']['dvs']
ts = data['ts']

#%%

for currentTime in range(9):
    aVariable = ts >= currentTime 
    print(currentTime, np.argmax(aVariable))
    
    

#%%
    
[False, True, True, False, True, False, True, False, True]


#%% 
differences = []   
for currentTime in range(9):
    firstIdx = np.argmax(ts >= currentTime)
    lastIdx = np.argmax(ts > currentTime + 1)
    #print(currentTime, firstIdx, lastIdx)
    print('time range: ' 
          + str(currentTime) + '-' + str(currentTime + 1)
          + ' first index: ' +  str(firstIdx)
          + ' last index: ' + str(lastIdx)
          + ' difference: ' + str(lastIdx - firstIdx))
    differences.append(lastIdx - firstIdx)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(differences)    
plt.ylim([0, max(differences)])
 
#%% 
period = 0.1
differences = []   
ourRange = np.arange(0, 9, period)
for currentTime in ourRange:
    firstIdx = np.argmax(ts >= currentTime)
    lastIdx = np.argmax(ts > currentTime + period)
    differences.append(lastIdx - firstIdx)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(ourRange, differences)    
plt.ylim([0, max(differences)])
    
#%%

from bimvee.plotEventRate import plotEventRate

plotEventRate(data, periods=[0.001, 0.01, 0.1, 1])




