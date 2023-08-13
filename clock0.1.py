import time

def show_clock():
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(current_time)
        time.sleep(1)

show_clock()
