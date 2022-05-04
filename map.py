import pandas as pd 
import tkinter as tk 
from PIL import ImageTk, Image

#df = pd.read_ex("cities.csv")
df = pd.read_excel("americancities.xls")
#pwith pd.ExcelWriter("americancities.xls") as writer:
    #df.to_excel(writer)

#print(df)


#
v = 1024/360 
v2 = 512/180

root = tk.Tk()

#print(df.columns)
latd = list(df["LatD"])
latm = list(df[' "LatM"'])
lats= list(df[' "LatS"'])
#print(latd)
lond = list(df[' "LonD"'])
lonm = list(df[' "LonM"'])
lons= list(df[' "LonS"'])

image = r"C:\Users\madzo\Desktop\pythonprgs\pythonclass22\earthmap.jpg"
map_image = ImageTk.PhotoImage(Image.open(image))

canavas = tk.Canvas(root,width=1024,height=512)
canavas.create_image(512,256,image=map_image)
canavas.pack()
def make_marker(lnd, ltd, lnm, ltm, lns, lts):
    lon = 512 - (v*(lnd + (lnm/60)+(lns/3600)))
    lat = 256 - (v2*(ltd + (ltm/60)+(lts/3600)))
    canavas.create_oval((lon-5,lat-5,lon+5,lat+5),fill="#ff0000")

for lnd, ltd, lnm, ltm, lns, lts in zip(lond, latd, lonm,latm,lons,lats):
    make_marker(lnd, ltd, lnm, ltm, lns, lts)




root.mainloop()