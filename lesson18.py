#countdown timer

import time
from idlelib.run import MyHandler

my_time = int(input("Enter your time in seconds"))
for x in reversed(range(0, my_time)):
    seconds = x % 60
    minutes = int(x /60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


# time.sleep(3)            #when i hit enter it waits for 3 seconds then it hits enter.
print("TIME IS UP")