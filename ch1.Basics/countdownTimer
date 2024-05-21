
import time

timer = int(input("Enter the time in seconds: "))
# this loop start from the time the user intered and loop by -1
for x in range(timer, 0, -1):
    # % 60 so we don't get anything above 60    
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # it's an interrput to make the program waits 1 second each time it prints
    time.sleep(1)
    
print("Time's up")