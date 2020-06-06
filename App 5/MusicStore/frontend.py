# Andrew Brown : Last Edited 6/6/2020
# This program stores song information:
# Title, Artist, Album, Year
#
# User Can:
# 
# View all records
# Search an entry
# Add an entry
# Update an entry
# Delete an entry
# Close

###############
## FRONT END ##
###############

from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), artist_text.get(), album_text.get(), year_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), artist_text.get(), album_text.get(), year_text.get())



window=Tk()   # Create the window that will hold all of our objects

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Artist")
l2.grid(row=1,column=0)

l3=Label(window,text="Album")
l3.grid(row=0,column=2)

l4=Label(window,text="year")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

artist_text=StringVar()
e2=Entry(window,textvariable=artist_text)
e2.grid(row=1,column=1)

album_text=StringVar()
e3=Entry(window,textvariable=album_text)
e3.grid(row=0,column=3)

year_text=StringVar()
e4=Entry(window,textvariable=year_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All",width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12, comand=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12, command=close_command)
b6.grid(row=7,column=3)


window.mainloop() # Wrap all widgets b/w this line and Tk() method
