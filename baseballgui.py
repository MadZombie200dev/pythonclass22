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
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import os

df1 = pd.read_csv("core\Batting.csv")
df2 = pd.read_csv("core\Pitching.csv")
df1 = df1[df1['yearID'] >= 1990]
df2 = df2[df2['yearID'] >= 1990]

options = []
opt = []

for i in df1.columns:
    options.append(str(i)+"_bat")
    opt.append(["df1",str(i)])
for i in df2.columns:
    options.append(str(i)+"_pitch")
    opt.append(["df2",str(i)])
options_index = dict(zip(options,opt))
print(options_index)
#print(options)

types = ["Histogram (only takes x)","Scater","Pie"]



root = tk.Tk()
root.configure(bg = "#050505")
fig , ax = plt.subplots(1,1)

frame1 = tk.Frame(master=root)

canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


toolbar = NavigationToolbar2Tk(canvas, frame1, pack_toolbar= False)
toolbar.update()

toolbar.pack(anchor="c")
canvas.get_tk_widget().place(relx= .5, rely=.5, relheight= .5, relwidth= .5, anchor= "c")
frame1.place(relx= .5, rely=.45, relheight= .5, relwidth= .5, anchor= "c")

def get_values(col_name):
    if options_index[str(col_name)][0] == 'df2':
        return df2[str(options_index[str(col_name)][1])] , str(options_index[str(col_name)][1])
    if options_index[str(col_name)][0] == 'df1':
        return df1[str(options_index[str(col_name)][1])] , str(options_index[str(col_name)][1])
def run_plt():
    x , x_n = get_values(clicked_x.get())
    y , y_n= get_values(clicked_y.get())
    type_plot = clicked_t.get()
    if type_plot == "Scater":
       
        #canvas.delete('all')
        plt.cla() 
        plt.title(f"{x_n} Vs. {y_n}")
        plt.xlabel(x_n)
        plt.ylabel(y_n)
        ax.scatter(x, y)
        canvas.draw()
        #plt.show()
    if type_plot == "Histogram (only takes x)": 
        #canvas.delete('all')
        plt.cla()
        plt.title(f"{x_n}")
        plt.xlabel(x_n)
        plt.ylabel("")
        ax.hist(x)
        canvas.draw()
        #plt.show()


clicked_x = tk.StringVar()
  
clicked_x.set("X")

clicked_y = tk.StringVar()
  
clicked_y.set("Y")

clicked_t = tk.StringVar()
  
clicked_t.set("Type")

drop_x = tk.OptionMenu( root , clicked_x, *options )
drop_x.pack()

drop_y = tk.OptionMenu( root , clicked_y , *options )
drop_y.pack()

drop_type = tk.OptionMenu( root , clicked_t, *types )
drop_type.pack()



button = tk.Button( root , text = "Run" , command = run_plt).pack()


frame2 = tk.Frame(master=root, bg="#262626")
enter_var = tk.StringVar()

lb= tk.Listbox(master=frame2, width = 120, bg="#262626",  bd=0, fg = "#127321")
lb.pack(side ="top")
entry = tk.Entry(frame2,textvariable=enter_var, width = 120, bg="#262626",  bd=0 , fg = "#127321")
entry.pack(side="bottom")

class cmds():
    def __init__(self):
        self.commands_long = ["Histogram","Piechart","ScatterPlot"]
        self.commands_short = ["Hist","Pie","Scatter"]
        self.command_dict = dict(zip(self.commands_long,self.commands_short))
    def Histogram(self,x):
        self.x , self.x_n = get_values(x)
        plt.cla()
        plt.title(f"{self.x_n}")
        plt.xlabel(self.x_n)
        plt.ylabel("")
        ax.hist(self.x)
        canvas.draw()
    def scatter(self,x,y):
        self.x , self.x_n = get_values(x)
        self.y , self.y_n = get_values(y)
        plt.cla() 
        plt.title(f"{self.x_n} Vs. {self.y_n}")
        plt.xlabel(self.x_n)
        plt.ylabel(self.y_n)
        ax.scatter(self.x, self.y)
        canvas.draw()
    def command_parse(self,string_cmd):
        self.string_cmd = string_cmd
        self.cmd_split = string_cmd.split(" ")
        if len(self.cmd_split) > 1:
            if self.cmd_split[0] == "hist":
                self.Histogram(self.cmd_split[1])
                return "running"
            elif self.cmd_split[0] == "scatter":
                self.scatter(self.cmd_split[1],self.cmd_split[2])
                return "running"
            else:
                return "invalid command"
        else:
            return "no data or invalid command"
cmdrun = cmds()
#cmdrun.command_parse("scatter H_bat yearID_bat")
t = False
def enter_r(event):
    global t
    if t == True:
        t = False
def enter(event):
    #print(event)
    global t
    if t == False:
        print(enter_var.get())
        lb.insert(lb.size()+1,str(enter_var.get()))
        lb.insert(lb.size()+1,str(cmdrun.command_parse(str(enter_var.get()))))
        t = True


root.bind('<Return>', enter)
root.bind('<KeyRelease-Return>', enter_r)

frame2.place(relx= .5, rely=.87, relheight= .2, relwidth= .5, anchor="c")
root.mainloop()