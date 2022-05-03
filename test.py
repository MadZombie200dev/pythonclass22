import pandas as pd 
import tkinter as tk 
from PIL import ImageTk, Image

df = pd.read_csv("cities.csv")
#print(df)


#
v = 1024/360 
v2 = 512/180

root = tk.Tk()

#print(df.columns)
latd = list(df["LatD"])
#print(latd)
lond = list(df[' "LonD"'])

image = r"C:\Users\madzo\Desktop\pythonprgs\pythonclass22\earthmap.jpg"
map_image = ImageTk.PhotoImage(Image.open(image))

canavas = tk.Canvas(root,width=1024,height=512)
canavas.create_image(512,256,image=map_image)
canavas.pack()
def make_marker(lon_in, lat_in):
    lon = 512 - (v*lon_in)
    lat = 256 - (v2*lat_in)
    canavas.create_oval((lon-5,lat-5,lon+5,lat+5),fill="#ff0000")

for x,y in zip(lond, latd):
    make_marker(x, y)




root.mainloop()