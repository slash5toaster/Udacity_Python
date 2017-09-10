import webbrowser
import time

timer_count = 3
break_count = 0

print ("Program started on " + time.ctime())
while break_count < timer_count:
    # print ("on break " + break_count)
    time.sleep(10)
    webbrowser.open("https://youtu.be/dOlrYz9cJMI")
    break_count = break_count + 1
