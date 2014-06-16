print("Hello World")

print("Dev Branch")

print("Name change")

#!/usr/bin/python 
import os 
import urllib 
google = os.popen('zenity --entry --text="Enter what you want to google: " --title="google.py"').read() 
google = urllib.quote(google) 
os.system('firefox http://www.google.com/search?q=%s' % (google))  