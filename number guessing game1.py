import random
print("the goal is between 0 and 100 ")
# target = int(input("please enter the target : "))
target = random.randint(0,100)
print(target)
guess = int(input("please enter the guess :"))
flage = False
while not flage:
    if target == guess:
        print("yes")
        flage=True
        break

    elif target < guess:
        print("the bigger guess is ")
        flage = False
        guess = int(input("please enter the guess :"))

    elif target > guess:
        print("the guess is smaller")
        flage = False
        guess = int(input("please enter the guess :"))
