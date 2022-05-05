import requests
import pandas as pd 
import json
import xmltodict
from bs4 import BeautifulSoup

data = requests.get("https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml").text
soup = BeautifulSoup(data,'xml')
soup.prettify()
p = soup.find_all('stateVector')
d = []
for i in p:
    h = i.text.split("\n")
    h.pop(0)
    h.pop(-1)
    d.append(h)


df = pd.DataFrame(data=d, columns=["EPOCH","X","Y","Z","X_DOT","Y_DOT","Z_DOT"])

print(df)