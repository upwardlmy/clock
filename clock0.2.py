import datetime
import time
import os

def clear_screen():
    # 清除屏幕上的内容（根据不同的操作系统）
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # 获取当前时间
    now = datetime.datetime.now()

    # 清除屏幕上的内容
    clear_screen()

    # 格式化时间并输出
    current_time = now.strftime("%H:%M:%S")
    print("当前时间：", current_time)

    # 暂停一秒钟
    time.sleep(1)
