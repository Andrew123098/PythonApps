#### WEBSITE BLOCKER : Andrew Brown : 6/1/2020
### This program is meant to block certain websites during work hours to keep me from procrastinating.
## It does this by editing a host file on my computer, however, I have disable my antivirus for this to work b/c
## anti-virus software like to protect host files. Not the best approach to a website blocker.
## To run on startup, use windows task scheduler (Udemy Lecture 154)
import time
from datetime import datetime as dt

host_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc"  # r in front is a roll (meaning you are not passing any special character s/a \n)
redirectMyIP="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "www.instagram.com", "intsagram.com"]

while True: # Always run this loop!
    # If time is between 8 o'clock and 4 o'clock (AKA working hours) then block websites
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16): 
        print("Working Hours...")
        with open(host_path, 'r+') as file:                                   # Open file for editing
            content=file.read()                                               # Save file contents to content variable
            for website in website_list:                                      # Loop through websites in the website list
                if website in content:                                        # If the wbesites are found in the file content
                    pass                                                      # Do nothing
                else:                                                         # Otherwise
                    file.write("#   " +redirectMyIP+ "      " +website+ "\n") # Write formatted content to file
    # If time is not working hours
    else:                                                               
        print("Fun hours...")                                       
        with open(host_path, 'r+') as file:                              # Open file for editing
            content=file.readlines()                                     # Save content as a list containing each line as a list item
            file.seek(0)                                                 # Move cursor to begining of file
            for line in content:                                         # Loop through the lines in the content variable
                if not any(website in line for website in website_list): # If none of the websites exist (loop through websites) in each line (any returns True/False)
                    file.write(line)                                     # Write the full line out
                file.truncate()                                          # End the file writing

    time.sleep(5)

