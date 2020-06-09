# Andrew Brown : Last Edited 6/8/2020
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
# Clear all entries
#
# NOTE: To create a .exe file, use the termial command 'pyinstaller --onefile --windowed frontend.py'

###############
## FRONT END ##
###############

from tkinter import *   # Import tkinter w/o need for tkinter prefix.
import backend          # Import functions from backend file.

## View all songs in the music library.
def view_command():
    list1.delete(0,END)        # Clear the list box.
    for row in backend.view(): # Loop through all rows returned by view function.
        list1.insert(END, row) # Insert each row as a different row in the list box.

## Seach for a song using one or more of the 4 information entries.
def search_command():
    list1.delete(0,END)         # Clear the list box. >> Loop through tuple returned by search function.
    for row in backend.search(title_text.get(), artist_text.get(), album_text.get(), year_text.get()):
        list1.insert(END, row)  # Insert each tuple in a row in the list box.

## Add song to music database
def add_command():
    backend.insert(title_text.get(), artist_text.get(), album_text.get(), year_text.get())     # Insert values from entry boxes into music library
    list1.delete(0,END)                                                                        # Clear the list box.
    list1.insert(END,(title_text.get(), artist_text.get(), album_text.get(), year_text.get())) # Insert values from entry boxes into list box.

## Update a song in the music library
def update_command(): ## >> Call backend update function with selected id and new values from the entry boxes.
    backend.update(selected_tuple[0],title_text.get(), artist_text.get(), album_text.get(), year_text.get()) 

## Delete a song from the music library
def delete_command():
    backend.delete(selected_tuple[0]) # Delete selected song from the database using song id

## Get tuple of selected row when user clicks on song in list box.
def get_selected_row(event):
    try:                                  
        global selected_tuple             # Save song tuple as a global variable
        index=list1.curselection()[0]     # Store song ID of selected song in index variable
        selected_tuple=list1.get(index)   # Store all song info in the tuple global variable
        e1.delete(0,END)                  ### Clear all the entry boxes and insert info from selected song
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:                    # If the user clicks in the listbox when there are no songs in the database (IndexError)
        pass                              # Do nothing

## Clear the entry boxes.
def clear_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

window=Tk() # Create the window that will hold all of our objects (All frontend GUI design goes b/w here and window.mainloop())

window.wm_title("Music Library") # Titles the Window

#################################
## LABELS:                     ##
## Create label in the window. ##
## Place lable on GUI grid.    ##
#################################

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Artist")
l2.grid(row=1,column=0)

l3=Label(window,text="Album")
l3.grid(row=0,column=2)

l4=Label(window,text="Year")
l4.grid(row=1,column=2)

###########################################################
## ENTRY BOXES:                                          ##
## Initialize storage variables as string variables      ##
## Create entry boxes in the window w/ storage variables ##
## Place entry boxes on GUI grid.                        ##
###########################################################

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

##########################################################
## LIST BOX:                                            ##
## Create list box in window and define dimensions.     ##
## Define list box placement and how many RxC it spans. ## 
##########################################################

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

##############################################################
## SCROLLBARS:                                              ##
## Create scrollbar in window.                              ##
## Place scrollbar on window grid.                          ##
## Set scroll bar to control y-axis scrolling of list1.     ##
## Set list one to take y-axis commands from the scrollbar. ##
##############################################################

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

sb2=Scrollbar(window, orient='horizontal') # Orients the scrollbar sideways in the GUI
sb2.grid(row=7,column=0,columnspan=2)
list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

## When I click on an item in the listbox, run the function get_selected_row.
list1.bind('<<ListboxSelect>>', get_selected_row)

#########################################################
## BUTTONS:                                            ##
## Create buttons in window with defined label, width, ##
## and funtion executed when pressed.                  ##
## Place button on GUI grid.                           ##
#########################################################

b1=Button(window,text="View All",width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Clear",width=12, command=clear_command)
b6.grid(row=7,column=3)


window.mainloop() # Wrap all widgets b/w this line and Tk() method
