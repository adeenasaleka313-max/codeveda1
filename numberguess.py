import random
number = random.randint(1, 100)

max_attempts = 5

print("Welecome to the guessing game!")
print("guess the number which I have choosen")
print("You have 5 attempts to guess")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt} : Enter your guess number:"))

    if guess == number:
        print("congratulations! your guess is correct")
        break
    elif guess > number:
        print("too high")
    else:
        print("too low")

print("game over!you have used all your attempts")
print("the number was:", number)

