
import time
from datetime import datetime as dt

host_temp=r"C:\Users\andre\OneDrive\Documents\Github\Learning Python\App 3"
host_path=r"C:\Windows\System32\drivers\etc"  # r in front is a roll (meaning you are not passing any special character s/a \n)
myIP="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "www.instagram.com", "intsagram.com"]

while True: # Always run this loop!
    # Only block websites between 8 o' clock and 4 o' clock
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16): 
        print("Working Hours...")
    else: 
        print("Fun hours...")  
    time.sleep(5)

