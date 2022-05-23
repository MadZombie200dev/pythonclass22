import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import pyplot as pt
import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

#fig = Figure(figsize=(5, 4), dpi=100)
#t = np.arange(0, 3, .01)
#fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
fig , ax = pt.subplots(1,2)

frame1 = tkinter.Frame(master=root,bg = "#00ff00")

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


toolbar = NavigationToolbar2Tk(canvas, frame1, pack_toolbar= False)
#toolbar.configure()
toolbar.update()
#toolbar.pack()
#canvas.
#frame1.pack()
#frame1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
toolbar.pack(anchor="c")
canvas.get_tk_widget().place(relx= .5, rely=.5, relheight= .5, relwidth= .5, anchor= "c")
frame1.place(relx= .1, rely=.1, relheight= .5, relwidth= .5, anchor= "c")


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.