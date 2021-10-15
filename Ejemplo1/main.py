import time
from datetime import datetime

# while True:
    # Print current time and sleep 1 minute
    def display():
        current_time = now.strftime("%H:%M:%S")
        current_date = today.strftime("%d %B, %Y")
        print("Today's date: ", current_date,"and ", "current time: ", current_time)
    t = Timer(60, display)
    t.start()
