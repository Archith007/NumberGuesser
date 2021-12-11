import random
#randoNumber = random.randint(1,9)
randoNumber = 5
chances = 0

while chances < 5:
    guess = int(input("enter your guess"))
    if guess == randoNumber:
        print("Congratulations You Win!")
        chances = 5
        #print(chances)
    elif guess > randoNumber:
        print("Pick A Smaller Number")
        chance = chances + 1
        #print(chances)
    else:
        print("Pick A Bigger Number")
        chances = chances + 1
        #5print(chances)
else:
    print("You Lose The Number Was", randoNumber)




