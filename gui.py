from tkinter import *
from tkinter import ttk
import tkinter as tk
from backend import *
from bs4 import BeautifulSoup as bs
from pywebcopy import save_website
from tkinter import messagebox
from tkhtmlview import HTMLLabel
from tkinter.ttk import Entry




#window creation
frame=Tk()
frame.title("Synapse")
frame.geometry("1260x820")
frame.config(bg="#00ADB5")

#frame creation
topframe=Frame(frame, bg="#222831", height='200', width='400',relief=SUNKEN, borderwidth=5)
topframe.pack(pady=25)

outputframe0=Frame(frame,bg="#393E46", width='1000',pady='10')
outputframe0.pack(anchor='center')

outputframe=Frame(outputframe0,bg="#393E46", width='1000',pady='10')
outputframe.pack(anchor='center')
responseframe = Frame(outputframe0, borderwidth=2, bg="#222831",)
responseframe.pack()
sframe = Frame(responseframe, padx=3, pady=3, bg="#fff", highlightbackground="black", highlightthickness=3)
sframe.pack()
statusframe = Frame(sframe, bg="white")
statusframe.pack()

# #label
# output=Label(outputframe,bg="pink",text="my output is here", height=1)
# output.pack(padx=200,pady =40)

#inputbox
myinput=Text(topframe, height=1.5,width=80)
myinput.grid(row=0,column=1,padx=35,pady=50)


def click():
    status = Label(statusframe, text= "Hello", height=1, width=16)
    status.pack()

#dropdown
def dropdown():
    newvar = clicked.get()
    return(newvar)


def saveinput():
    url = myinput.get(1.0, "end-1c")
    param =tab1.get(1.0, "end-1c")
    auth = tab2.get(1.0, "end-1c")
    head =tab3.get(1.0, "end-1c")
    json1 =tab4.get(1.0, "end-1c")
    drop = dropdown()
    code,text,header = request(drop, url ,auth, head,param,json1) 
    soup =bs(text, 'html.parser')
    prettyHTML = soup.prettify()
    lbl1.delete("1.0" , "end")
    lbl1.insert(tk.END, prettyHTML)
    lbl3.delete("1.0" , "end")
    lbl3.insert(tk.END, header)
    lbl2.set_html(text)
    status.config(text="Status Code :"+str(code))
    

def saveproject():
    link = myinput.get(1.0, "end-1c")
    save_website(url = link, project_folder="./saved_folder/")
    messagebox.showinfo("Sucess!","Project folder saved")


#buttom
sendButton = Button(topframe, text="Send",command=saveinput, padx= 5, pady=5, bg = "#EEEEEE", fg = "black",font=('Arial Rounded MT Bold',10,'normal'))
sendButton.grid(row=0, column=2)
saveButton = Button(topframe, text="Save",command=saveproject, padx= 8, pady=5, bg = "#EEEEEE", fg = "black",font=('Arial Rounded MT Bold',10,'normal'))
saveButton.grid(row=0, column=3)





option = [
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE"
]

#data type of Menu Text()
clicked = StringVar()

# initial menu text
clicked.set("GET")

# dropdown menu
drop = OptionMenu(topframe, clicked, *option, command=dropdown)
drop.grid(row=0, column=0)
drop.config(bg = "#00ADB5", fg = "black", padx = 15, pady=15,  font=('Arial Black',12,'normal'))


# tabs widget
tabControl = ttk.Notebook(outputframe, height=100, width=1700)
tab1 = Text(tabControl, width=1000)
tab2 = Text(tabControl, width=1000)
tab3 = Text(tabControl, width=1000)
tab4 = Text(tabControl, width=1000)
tabControl.add(tab1, text='Params')
tabControl.add(tab2, text='Authorization')
tabControl.add(tab3, text='Headers')
tabControl.add(tab4, text='JSON')
tabControl.pack(fill="both", padx=400, pady=10)




#tabs widget
tabControl= ttk.Notebook(responseframe, height = 700, width = 1200)
tab_1 = Label(tabControl, text="", bg="#fff")
tab_2 = Label(tabControl, text="", bg="#fff")
tab_3 = Label(tabControl, text="", bg="#fff")
tabControl.add(tab_1, text='Raw')
tabControl.add(tab_2, text='Preview')
tabControl.add(tab_3, text='Headers')
tabControl.pack(fill = "both")


#status code creation
status = Label(statusframe, text= "Status Code: 000", height =1, width =16)
status.pack()

#label creation
lbl1 =Text(tab_1, height=1150,width =100,padx=50,pady=50, bg="#fff",fg="black", font="Helvetica")
lbl1.pack()
lbl2 =HTMLLabel(tab_2,html = "preview", height=1150,width =100,padx=50,pady=50, bg="#fff",fg="black", font="Helvetica")
lbl2.pack( anchor= "center")
lbl3 =Text(tab_3, height=1150,width =100,padx=50,pady=50 ,bg="#fff",fg="black", font="Helvetica")
lbl3.pack()


frame.mainloop()