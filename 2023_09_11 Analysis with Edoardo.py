# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:35:09 2023

@author: sbamford
"""

from random import random

import numpy as np

#%% Decide random coords for emitters and receivers

emitters = []

receivers = []

numReceivers = 10

numEmitters = 10

for emitter in range(numEmitters):
    x = v
    y = random()
    coords = (x, y)
    emitters.append(coords)

emitters = np.array(emitters)
    
for receiver in range(numReceivers):
    x = random()
    y = random()
    coords = (x, y)
    receivers.append(coords)
    
receivers = np.array(receivers)

#%% Alternatively, place emitters and receivers around a circle

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

  

#%%  Plot emitters and receivers, and all the rays that connect them
# Choose two rays to highlight in red
    
import matplotlib.pyplot as plt

plt.close('all')

fig, ax = plt.subplots()

ax.plot(receivers[:, 0], receivers[:, 1], 'o')
ax.plot(emitters[:, 0], emitters[:, 1], 'x')


redEmitter = True
for emitter in range(numEmitters):
    for receiver in range(numReceivers):
        if random() < 0.04:
            rayColour = 'r'
        else:
            rayColour = 'k'
        plt.plot([emitters[emitter, 0], receivers[receiver, 0]],
                 [emitters[emitter, 1], receivers[receiver, 1]],
                 rayColour)
        
    

    