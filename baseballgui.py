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

test_data_x , test_data_y = range(1,101),range(1,101)


root = tk.Tk()




root.mainloop()






'''#h = open("core\Batting.csv","r").read()
df5 = pd.read_csv("core\TeamsFranchises.csv") #.set_index("franchID")
df6 = pd.read_csv("core\SeriesPost.csv")
dictt = dict(df6['teamIDwinner'].value_counts())
team, wins = dictt.keys() , dictt.values()
print()
#print



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
fig, ax = plt.subplots(2,3)
ax[0][0].pie(wins, explode= , labels=team, autopct='%1.1f%%')
#ax[0].hist(df4['W'], bins=n_bins)
plt.show()
#print(df4)'''