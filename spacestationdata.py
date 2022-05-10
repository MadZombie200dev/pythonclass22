import requests
import pandas as pd 
import json
import xmltodict
import numpy as np
import math
import tkinter as tk 
from PIL import ImageTk, Image
from bs4 import BeautifulSoup

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
    print(h)
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


df["phi"] = phi_list
df["lat"] = lat_list
df["lon"] =  df["phi"]
#print(df)
def filter_by(column,data,max):
    return data[data[column] <= max] 


    
print(filter_by('radius', df, 6790))




v = 1024/360 
v2 = 512/180

root = tk.Tk()

image = r"C:\Users\madzo\Desktop\pythonprgs\pythonclass22\earthmap.jpg"
map_image = ImageTk.PhotoImage(Image.open(image))

canavas = tk.Canvas(root,width=1024,height=512)
canavas.create_image(512,256,image=map_image)
canavas.pack()
def make_marker(lon1,lat1):
    lon = 512 - (v*(lon1))
    lat = 256 - (v2*(lat1))
    canavas.create_oval((lon-5,lat-5,lon+5,lat+5),fill="#ff0000")

for lon, lat in zip(df["lon"],df["lat"]):
    make_marker(lon,lat)
root.mainloop()