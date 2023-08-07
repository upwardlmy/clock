import time

def start_timer(duration):
    """开始计时"""
    remaining_time = duration * 60
    while remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"\r{minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)
        remaining_time -= 1
    print("\n专注时间结束！")

def main():
    print("欢迎使用专注时钟！")
    duration = int(input("请输入专注时长（单位：分钟）: "))
    start_timer(duration)

if __name__ == "__main__":
    main()
