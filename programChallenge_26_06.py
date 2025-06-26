import requests
import math
print("Alfred's game")

def logic():
    num1 = int(input("Input number 1: "))
    num2 = int(input("Input number 2: "))
    num3 = int(input("Input number 3: "))

    nums = [num1, num2, num3]

    # Get a random integer from random.org between 1 and 3 (inclusive)
    response = requests.get("https://www.random.org/integers/?num=1&min=1&max=3&col=1&base=10&format=plain&rnd=new")
    psudorand = int(response.text.strip())

    avg = (num1 + num2 + num3)/3

    top = max(nums)

    low = min(nums)

    if psudorand == 1:
        print("Well done you win with " + str(top*2))
    elif psudorand == 2:
        print("Good result all round " + str(avg) + " You get a draw")
    else:
        print("You are pathetic with " + str(math.floor(low/2)))

logic()
