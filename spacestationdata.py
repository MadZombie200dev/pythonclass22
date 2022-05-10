import requests
import pandas as pd 
import json
import xmltodict
import numpy as np
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

df["radius"] = radi(df["X"], df["Y"], df["Z"])
df["speed"] = find_speed(df["X_DOT"], df["Y_DOT"], df["Z_DOT"])
print(df)
def filter_by(column,data,max):
    return data[data[column] <= max] 
print(filter_by('radius', df, 6790))