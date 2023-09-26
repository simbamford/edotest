# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:16:04 2023

@author: sbamford
"""

#%% Import the data

import numpy as np
from scipy import  io

dictFromMatlab = io.loadmat("C:\\Data\\Trial_44.mat")
data = dictFromMatlab['Data']
ts = data[:, 0] 
samples = data[:, 3:]

#%% Quick visualisation of the data

import matplotlib.pyplot as plt

print(np.max(np.array(dictFromMatlab['Acq'])))

plt.close('all')
plt.plot(ts, samples[:, 0], '-o')

#%% Manually find data for first frame, and do surface plot

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

plt.close('all')

firstFrame = samples[:165, :]


fig = plt.figure()
ax = plt.axes(projection='3d')

y = np.arange(len(firstFrame))
x = np.arange(len(firstFrame[0]))

(x ,y) = np.meshgrid(x,y)

ax.plot_surface(x,y,firstFrame)
plt.show()

#%% Manually find data for second frame and do surface plot

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

secondFrame = samples[225:389, :]

fig = plt.figure()
ax = plt.axes(projection='3d')

y = np.arange(len(secondFrame))
x = np.arange(len(secondFrame[0]))

(x ,y) = np.meshgrid(x,y)

ax.plot_surface(x,y,secondFrame)
plt.show()


#%% Show first and second frames as images side by side


fig, axes = plt.subplots(1,2)

axes[0].imshow(firstFrame)
axes[1].imshow(secondFrame)


#%% compress the first frame in time, to have one sample per emitter
'''
We see that there is a change of emitter every 6.83 samples;
we'll use this observation manually for now; we may
automate this detection later

we'll also scale the 12 bit data into the range 0-1
'''

chosenSamples = np.arange(6.83, 164, 6.83).astype(int)

firstFrameCompressed = firstFrame[chosenSamples, :]
firstFrameCompressed = firstFrameCompressed / 4096

#%% Create coordinates for emitters and receivers around a circle

from random import random
import numpy as np

numReceivers = 24
numEmitters = numReceivers

emitters = []
receivers = []

for element in range(numReceivers):
    proportionAroundTheCircle = element / numReceivers * np.pi * 2
    x = np.sin(proportionAroundTheCircle)
    y = np.cos(proportionAroundTheCircle)
    emitters.append((x, y))
    proportionAroundTheCircle = (element + 0.5) / numReceivers * np.pi * 2
    x = np.sin(proportionAroundTheCircle)
    y = np.cos(proportionAroundTheCircle)
    receivers.append((x, y))
    
emitters = np.array(emitters)
receivers = np.array(receivers)

#%% Plot the coordinates around a circle

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
plt.close('all')

fig, ax = plt.subplots()

ax.plot(receivers[:, 0], receivers[:, 1], 'o')
ax.plot(emitters[:, 0], emitters[:, 1], 'x')

    
#%% Plot the first two frames in ray form side by side        
'''
We see that there is a change of emitter every 6.83 samples;
we'll use this observation manually for now; we may
automate this detection later
'''

chosenSamples = np.arange(6.83, 164, 6.83).astype(int)
#chosenSamples = np.arange(7, 164, 7).astype(int)

fig, axes = plt.subplots(1,2)

for frame, ax in zip([firstFrame, secondFrame], axes):

    frameCompressed = frame[chosenSamples, :] / 4096
    for emitter in range(numEmitters):
        for receiver in range(numReceivers):
            rayColour = cm.rainbow(frameCompressed[emitter, receiver])
            x = [emitters[emitter, 0], receivers[receiver, 0]]
            y = [emitters[emitter, 1], receivers[receiver, 1]]
            ax.plot(x, y, color=rayColour)


'''
Insert here a reliable method of identifying the start of each sample
'''

#%%


plt.close('all')
plt.plot(np.arange(0, firstFrame.shape[0]), firstFrame[:, 23], '-o')
plt.plot(chosenSamples, firstFrame[chosenSamples, 23], 'ro')

#%% Find the indices of the first sample of every frame
            
thresholdForFrameData = 200 # An empirical choice
frameStartIds = np.where(np.logical_and(samples[1:, 0] > thresholdForFrameData, 
                    samples[:-1, 0] < thresholdForFrameData))[0]


#%% Generalise to other frames
        
'''
We see that there is a change of emitter every 6.83 samples;
we'll use this observation manually for now; we may
automate this detection later
'''

plt.close('all')

numFramesToProcess = 5 
'''# Alternatively we could process all of them, 
but then we need to save the plots to disk and close them inside the loop
'''
for idx, frameStartIdx in enumerate(frameStartIds[:5]):
    frame = samples[frameStartIdx:frameStartIdx+165,:]
    fig, ax = plt.subplots()
    frameCompressed = frame[chosenSamples, :] / 4096
    for emitter in range(numEmitters):
        for receiver in range(numReceivers):
            rayColour = cm.rainbow(frameCompressed[emitter, receiver])
            x = [emitters[emitter, 0], receivers[receiver, 0]]
            y = [emitters[emitter, 1], receivers[receiver, 1]]
            ax.plot(x, y, color=rayColour)



        