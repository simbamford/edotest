# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:16:04 2023

@author: sbamford
"""

import numpy as np
from scipy import  io

xx = io.loadmat("C:\\Data\\Trial_44.mat")


import matplotlib.pyplot as plt

#plt.imshow(xx['LED_offset'])

print(np.max(np.array(xx['Acq'])))

plt.close('all')
plt.plot(xx['Data'][:, 0], xx['Data'][:, 4])


#%%

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#plt.close('all')

firstFrame = xx['Data'][:165, 3:27]


fig = plt.figure()
ax = plt.axes(projection='3d')

y = np.arange(len(firstFrame))
x = np.arange(len(firstFrame[0]))

(x ,y) = np.meshgrid(x,y)

ax.plot_surface(x,y,firstFrame)
plt.show()

#%%

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


secondFrame = xx['Data'][225:389, 3:27]

fig = plt.figure()
ax = plt.axes(projection='3d')

y = np.arange(len(secondFrame))
x = np.arange(len(secondFrame[0]))

(x ,y) = np.meshgrid(x,y)

ax.plot_surface(x,y,secondFrame)
plt.show()


#%%


fig, axes = plt.subplots(1,2)

axes[0].imshow(firstFrame)
axes[1].imshow(secondFrame)


#%%


# importing matplot lib
import matplotlib.pyplot as plt
import numpy as np
 
# importing movie py libraries
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
 
# numpy array
x = np.linspace(-2, 2, 200)
 
# duration of the video
duration = 2
 
# matplot subplot
fig, ax = plt.subplots()
 
# method to get frames
def make_frame(t):
     
    # clear
    ax.clear()
     
    # plotting line
    ax.plot(x, np.sinc(x**2) + np.sin(x + 2 * np.pi / duration * t), lw = 3)
    ax.set_ylim(-1.5, 2.5)
     
    # returning numpy image
    return mplfig_to_npimage(fig)
 
# creating animation
animation = VideoClip(make_frame, duration = duration)
 
# displaying animation with auto play and looping
animation.ipython_display(fps = 20, loop = True, autoplay = True)

#%% compress the first frame in time, to have one sample per emitter
'''
We see that there is a change of emitter every 6.83 samples;
we'll use this observation manually for now; we may
automate this detection later
'''

chosenSamples = np.arange(6.83, 164, 6.83).astype(int)

firstFrameCompressed = firstFrame[chosenSamples, :]
firstFrameCompressed = firstFrameCompressed / 4096

#%% Plot in ray form

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

#%% Plot the first frame

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
plt.close('all')

fig, ax = plt.subplots()

ax.plot(receivers[:, 0], receivers[:, 1], 'o')
ax.plot(emitters[:, 0], emitters[:, 1], 'x')

for emitter in range(numEmitters):
    for receiver in range(numReceivers):
        rayColour = cm.rainbow(firstFrameCompressed[emitter, receiver])
        x = [emitters[emitter, 0], receivers[receiver, 0]]
        y = [emitters[emitter, 1], receivers[receiver, 1]]
        plt.plot(x, y, color=rayColour)
    
#%% P,ot the second frame as well
        
fig, axes = plt.subplots(1,2)

axes[0].imshow(firstFrame)
axes[1].imshow(secondFrame)




        