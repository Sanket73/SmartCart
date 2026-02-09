#Guess the Number 

import random

target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the target :"))
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Yor number is so small. Take a bigger guess....!")
    else:
        print("Yor number is so big. Take a smaller guess....!")

print("!......GAME IS OVER.......!")