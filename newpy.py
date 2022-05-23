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

data = requests.get("https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml").text
soup = BeautifulSoup(data,'xml')
soup.prettify()
p = soup.find_all('stateVector')
d = []
for i in p:
    h = i.text.split("\n")
    #print(h)
    
    h.pop(0)
    h.pop(-1)
    l = h[0] 

    h = list(map(float,h[1:7]))
    h = [l] + h
    #print(h)
    d.append(h)


df = pd.DataFrame(data=d, columns=["EPOCH","X","Y","Z","X_DOT","Y_DOT","Z_DOT"])


def radi(x_in,y_in,z_in):
    r = np.sqrt((x_in*x_in)+(y_in*y_in)+(z_in*z_in))
    return r

def find_speed(x_in,y_in,z_in):
    r = np.sqrt((x_in*x_in)+(y_in*y_in)+(z_in*z_in))
    return r

def phi(x_in,y_in,z_in):
    #print(type(x_in))
    if x_in > 0:
        o = math.atan(y_in / x_in)
    elif x_in < 0 and y_in >= 0: 
        o = math.atan(y_in / x_in) + math.pi
    elif x_in < 0 and y_in < 0:
        o = math.atan(y_in / x_in) - math.pi
    return o * (180/math.pi)
def theta(x_in,y_in,z_in):
    return np.arctan(np.sqrt((x_in*x_in)+(y_in*y_in))/z_in) * (180/math.pi)
def this_is_dumb(theta):
    if theta > 0:
        t = theta -90
    if theta < 0:
        t = theta + 90
    return t
def get_day(epoch):
    e = epoch.split("-").pop(-1)
    #print(e)
    e = e.split("T")
    #print(e)
    return float(e[0])

df["radius"] = radi(df["X"], df["Y"], df["Z"])
df["speed"] = find_speed(df["X_DOT"], df["Y_DOT"], df["Z_DOT"])
#df["phi"] =phi(df["X"], df["Y"], df["Z"])
phi_list = []
for x,y,z in zip(df["X"], df["Y"], df["Z"]):
    phi_list.append(phi(x, y, z))
df["theta"] =theta(df["X"], df["Y"], df["Z"])

lat_list = []
for i in df["theta"]:
    lat_list.append(this_is_dumb(i))

day_list = []
for i in df["EPOCH"]:
    day_list.append(get_day(i))

df["phi"] = phi_list
df["day"] = day_list
df["lat"] = lat_list
df["lon"] =  df["phi"]
#print(df)
def filter_by(column,data,max):
    return data[data[column] == max] 
df = filter_by('day', df, 136)

fig, ax = plt.subplots(2,2)



ax[0][0].plot(list(df["X"]),list(df["X_DOT"]), "ro")
ax[0][1].plot(list(df["radius"]),list(df["speed"]), "ro")
ax[1][0].plot(list(df["lat"]),list(df["speed"]), "ro")
ax[1][1].plot(list(df["lon"]),list(df["speed"]),"ro")
#ax[0][2].plot(list(df["lon"]),list(df["speed"]),"ro")
plt.show()

print(df)



    





v = 1024/360 
v2 = 512/180

#root = tk.Tk()

#image = r"C:\Users\madzo\Desktop\pythonprgs\pythonclass22\earthmap.jpg"
#map_image = ImageTk.PhotoImage(Image.open(image))

#canavas = tk.Canvas(root,width=1024,height=512)
#canavas.create_image(512,256,image=map_image)
#canavas.pack()




'''

def make_marker(lon1,lat1,r):
    #frame = tk.Frame(root,width=10, height=10)
    lon = 512 - (v*(lon1))
    lat = 256 - (v2*(lat1))
    minh = min(df["radius"])
    maxh = max(df["radius"])
    rangecolor = 255
    col = str(hex(int(((r-minh)/(maxh-minh))*255)))[2::]
    if len(col) == 1:   
        col = "0" + col

    #print(col)

    canavas.create_oval((lon-5,lat-5,lon+5,lat+5),fill=f"#{col}0000")
    j = [int(lon-5),int(lat-5),int(lon+5),int(lat+5)]
    return j
'''

h = {}

#for lon, lat, day,r,ind in zip(df["lon"],df["lat"],df["day"],df["radius"],df.index):
    #if day == 132:
        #print(ind)
        #h[ind]= make_marker(lon,lat,r)
#print()
#label = tk.Label(canavas, bg = "grey", bd = 10)
#label = tk.Label(canavas, bg = "grey", bd = 10)
'''
def printme(event):
   
    text = ""
    valid = False
    
    for index, value in h.items():
        if event.x < value[2] and event.x > value[0] and event.y < value[3] and event.y > value[1]:
            point_data = df.iloc[index]
            valid = True
            text = text + f"Longitude: {int(point_data['lon'])} \n Latitude: {int(point_data['lat'])} \n Speed: {int(point_data['speed'])} \n Day: {str(point_data['EPOCH'])} \n -----------------------\n"
    if valid == True:
        label['text'] = text
        label.place(x = event.x, y = event.y)
    if valid == False:
        #label.place_forget()]
'''


#o = canavas.bind("<Button-1>", printme)

#root.mainloop()