import random
number = random.randint(1,9)
chances=0

print("Guess a number between 1-9: ")

while chances<5:
    guess=int(input("Guess a number between 1 and 9: "))
    if guess== number:
        print("Congratulations You guessed the right number!!!")
        break
    elif guess>number:
        print("Guess a smaller number.")
    elif guess<number:
        print("Guess a greater number.")

    chances+=1  

if(chances>5):
    print("you lose.")