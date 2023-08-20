import random

def guess_number():
    number = random.randint(1, 100)
    chances = 5

    while chances > 0:
        guess = int(input("猜一个1到100之间的数字："))

        if guess < number:
            print("太小了！")
        elif guess > number:
            print("太大了！")
        else:
            print("恭喜你，猜对了！")
            return
        
        chances -= 1
        print("还剩下", chances, "次机会\n")
        
    print("游戏结束，你没有猜对。正确答案是", number)

guess_number()
