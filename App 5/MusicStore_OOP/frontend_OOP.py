# Andrew Brown : Last Edited 6/12/2020
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

###################
## FRONT END OOP ##
###################

from tkinter import *  # Import tkinter library w/o need for tkiner prefix for functions.
from backend_OOP import Database  # Import functions from backend file.

database=Database("music.db")  # Object created for the class

class Window(object):

    def __init__(self,window):

        self.window=window

        self.window.wm_title("Music Library") # Titles the Window

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

        self.title_text=StringVar()
        self.e1=Entry(window,textvariable=self.title_text)
        self.e1.grid(row=0,column=1)

        self.artist_text=StringVar()
        self.e2=Entry(window,textvariable=self.artist_text)
        self.e2.grid(row=1,column=1)

        self.album_text=StringVar()
        self.e3=Entry(window,textvariable=self.album_text)
        self.e3.grid(row=0,column=3)

        self.year_text=StringVar()
        self.e4=Entry(window,textvariable=self.year_text)
        self.e4.grid(row=1,column=3)

        ##########################################################
        ## LIST BOX:                                            ##
        ## Create list box in window and define dimensions.     ##
        ## Define list box placement and how many RxC it spans. ## 
        ##########################################################

        self.list1=Listbox(window,height=6,width=35)
        self.list1.grid(row=2,column=0, rowspan=6, columnspan=2)

        ##############################################################
        ## SCROLLBARS:                                              ##
        ## Create scrollbar in window.                              ##
        ## Place scrollbar on window grid.                          ##
        ## Set scroll bar to control y-axis scrolling of list1.     ##
        ## Set list one to take y-axis commands from the scrollbar. ##
        ##############################################################

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        sb2=Scrollbar(window, orient='horizontal') # Orients the scrollbar sideways in the GUI
        sb2.grid(row=7,column=0,columnspan=2)
        self.list1.configure(xscrollcommand=sb2.set)
        sb2.configure(command=self.list1.xview)

        ## When I click on an item in the listbox, run the function get_selected_row.
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #########################################################
        ## BUTTONS:                                            ##
        ## Create buttons in window with defined label, width, ##
        ## and funtion executed when pressed.                  ##
        ## Place button on GUI grid.                           ##
        #########################################################

        b1=Button(window,text="View All",width=12, command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window,text="Search Entry",width=12, command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window,text="Add Entry",width=12, command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window,text="Update",width=12, command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window,text="Delete",width=12, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window,text="Clear",width=12, command=self.clear_command)
        b6.grid(row=7,column=3)

    
    ## View all songs in the music library.
    def view_command(self):
        self.list1.delete(0,END)         # Clear the list box.
        for row in database.view():      # Loop through all rows returned by view function.
            self.list1.insert(END, row)  # Insert each row as a different row in the list box.

    ## Seach for a song using one or more of the 4 information entries.
    def search_command(self):
        self.list1.delete(0,END)         # Clear the list box. >> Loop through tuple returned by search function.
        for row in database.search(self.title_text.get(), self.artist_text.get(), self.album_text.get(), self.year_text.get()):
            self.list1.insert(END, row)  # Insert each tuple in a row in the list box.

    ## Add song to music database
    def add_command(self):
        database.insert(self.title_text.get(), self.artist_text.get(), self.album_text.get(), self.year_text.get())         # Insert values from entry boxes into music library
        self.list1.delete(0,END)                                                                                            # Clear the list box.
        self.list1.insert(END,(self.title_text.get(), self.artist_text.get(), self.album_text.get(), self.year_text.get())) # Insert values from entry boxes into list box.

    ## Update a song in the music library
    def update_command(self): ## >> Call backend update function with selected id and new values from the entry boxes.
        database.update(selected_tuple[0],self.title_text.get(), self.artist_text.get(), self.album_text.get(), self.year_text.get()) 

    ## Delete a song from the music library
    def delete_command(self):
        database.delete(selected_tuple[0]) # Delete selected song from the database using song id

    ## Clear the entry boxes.
    def clear_command(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)

    ## Get tuple of selected row when user clicks on song in list box.
    def get_selected_row(self, event):
        try:                                  
            global selected_tuple                  # Save song tuple as a global variable
            index=self.list1.curselection()[0]     # Store song ID of selected song in index variable
            selected_tuple=self.list1.get(index)   # Store all song info in the tuple global variable
            self.e1.delete(0,END)                  ### Clear all the entry boxes and insert info from selected song
            self.e1.insert(END,selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,selected_tuple[4])
        except IndexError:                         # If the user clicks in the listbox when there are no songs in the database (IndexError)
            pass                                   # Do nothing

#########################################################################################################################################

window=Tk() # Create the window that will hold all of our objects (All frontend GUI design goes b/w here and window.mainloop())
Window(window) # Call the init method of the Window class.
window.mainloop() # Wrap all widgets b/w this line and Tk() method
