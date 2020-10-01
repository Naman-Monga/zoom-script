#mypy
from datetime import datetime
import webbrowser
from csv import reader
import time
import os

# Your class duration in seconds

class_duration = 3000 

# Main function to read csv file and launch browser
def zoom_launcher():
    with open('schedule.csv','r') as schedule:
        csvreader = reader(schedule)
        now = datetime.now()
        current_time = now.strftime('%H:%M')
        day = now.strftime('%A')

        for row in csvreader:
            if row[0] == day:
                if current_time==row[2]:
                    zoom_link = row[1]
                    webbrowser.open(zoom_link)
                    return 1
    return 0

counter = 0
while(True):
    counter+=1
    triggered = zoom_launcher()
    time.sleep(5)
    
    # Printing the loop counter just for satisfaction.
    print('check '+str(counter))
    
    if triggered == 1:
        print('You have joined a class, going to sleep :) zzz')
        time.sleep(class_duration)
        triggered = 0
        # Terminate the meeting once time is up
        os.system("TASKKILL /F /IM Zoom.exe")
        time.sleep(0.5)
        
