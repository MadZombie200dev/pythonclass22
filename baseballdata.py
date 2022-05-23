import requests
import pandas as pd 
import json
import xmltodict
import numpy as np
import math
import tkinter as tk 
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

#h = open("core\Batting.csv","r").read()

df = pd.read_csv("core\Batting.csv")
df2 = pd.read_csv("core\PitchingPost.csv")
df3 = pd.read_csv("core\Teams.csv")
df["BatAv"] = df["H"]/df["G"]
df["HRG"] = df["HR"] /df["G"]
#df.sort_values(by=["BatAv"])

highest_batav = df.iloc[df["BatAv"].idxmax()]
most_hr = df.iloc[df["HR"].idxmax()]
most_hrg = df.iloc[df["HRG"].idxmax()]
min_era = df2.iloc[df2["ERA"].idxmin()]

df4=df3.query("teamID == 'NYA'").set_index('yearID').filter(items=['W'])

n_bins = df4.iloc[df2["W"].idxmax()]["W"]

fig, ax = plt.subplots(1,2)
ax[1].plot(df4.index,df4["W"])
ax[0].hist(df4['W'], bins=n_bins)
plt.show()
print(df4)