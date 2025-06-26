import requests
import random
import math
print("Alfred's game")

def logic():
    num1 = int(input("Input number 1: "))
    num2 = int(input("Input number 2: "))
    num3 = int(input("Input number 3: "))

    nums = [num1, num2, num3]

    psudorand = random.randrange(1, 3)

    avg = (num1 + num2 + num3)/3

    top = max(nums)

    low = min(nums)

    if psudorand == "1":
        print("Well done you win with"+ top*2)
    elif psudorand == "2":
        print("Good result all round "+ avg + " You get a draw")
    else:
        print("You are pathetic with "+str(math.floor(low/2)))

logic()