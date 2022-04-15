# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:19:56 2022

@author: hkopansk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir(r"C:\Users\hkopansk\OneDrive - Biogen\Documents\Python Data")

df_oldfaithful = pd.read_csv("oldfaithful.csv")

A = [55, 3]
B = [50, 3]

fig, axes = plt.subplots(2, 2, figsize=(10, 10), dpi = 200)

sns.scatterplot(data = df_oldfaithful, x = "INTERVAL", y = "DURATION", ax = axes[0,0])
axes[0,0].scatter(A[0], A[1], color = 'red')
axes[0,0].scatter(B[0], B[1], color = 'red')

def point_dist(x, y, x1, y1):
    h = ((x1 - x)**2 + (y1 - y)**2)**0.5
    return h


df_oldfaithful["Closer Point"] = 0.0
df_oldfaithful["A dist"] = 0
df_oldfaithful["B dist"] = 0


for i in range(10):
    for i in range(107):
        df_oldfaithful["A dist"][i] = point_dist(df_oldfaithful["INTERVAL"][i], df_oldfaithful["DURATION"][i], A[0], A[1])
        df_oldfaithful["B dist"][i] = point_dist(df_oldfaithful["INTERVAL"][i], df_oldfaithful["DURATION"][i], B[0], B[1])
    
    for i in range(107):
        if df_oldfaithful["A dist"][i] > df_oldfaithful["B dist"][i]:
            df_oldfaithful["Closer Point"][i] = "B"
        else:
            df_oldfaithful["Closer Point"][i] = "A"
        
    A = [np.mean(df_oldfaithful[df_oldfaithful["Closer Point"] == "A"]["INTERVAL"]), 
         np.mean(df_oldfaithful[df_oldfaithful["Closer Point"] == "A"]["DURATION"])]
    B = [np.mean(df_oldfaithful[df_oldfaithful["Closer Point"] == "B"]["INTERVAL"]), 
         np.mean(df_oldfaithful[df_oldfaithful["Closer Point"] == "B"]["DURATION"])]


sns.scatterplot(data = df_oldfaithful, x = "INTERVAL", y = "DURATION", hue = "Closer Point", ax = axes[0, 1])
axes[0,1].scatter(A[0], A[1],  color = 'red', marker = "x")
axes[0,1].scatter(B[0], B[1],  color = 'red', marker = "x")

sns.kdeplot(data = df_oldfaithful, x = "INTERVAL", hue = "Closer Point", ax = axes[1,0])
sns.kdeplot(data = df_oldfaithful, x = "DURATION", hue = "Closer Point", ax = axes[1,1])