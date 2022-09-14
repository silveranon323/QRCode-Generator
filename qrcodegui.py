from tkinter import*
import pyqrcode as df
#import png
root = Tk()
root.config(bg = "black")
root.minsize(600,175)
root.maxsize(600,175)

def submit():
     x = userdat.get()
     a = df.create(x)
     qrname = locdat.get()
     saku = ('"{}"'.format(qrname))
     a.png("  .png")

mylabel = Label(root , text = "QR CODE GENERATOR" , font =( "comic sans ms" , 25 ) , bg = "black",fg = "#29C0FF")
mylabel.pack()
url = Label(root , text = "Enter the Data : ",fg = "#15FF28", bg = "black").pack()
userdat = StringVar()
locdat = StringVar()
e = Entry(root , bg ="white" , fg = "green"  , textvariable = userdat ,selectbackground = "black",width = 30 ,borderwidth = 2 )
e.place( x = 360 ,y = 50)
url = Label(root , text = "Enter the Name of the QR Code : ",fg = "#15FF28", bg = "black").pack()
f = Entry(root , bg ="white" , fg = "green"  , textvariable = locdat ,selectbackground = "black",width = 30 ,borderwidth = 2 )
f.place( x = 397 ,y =70)
Button(root , text = "Submit", command = submit).pack()


root.mainloop()
