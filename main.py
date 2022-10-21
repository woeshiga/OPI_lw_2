"""
developer: woeshiga
"""

rom random import randint

name = input("Enter your name: ")

age = input("Enter your age: ")

hobby = input("Enter your hobby: ")

print(f"Your name is {name}\nYour age is {age}\nYour hobby is {hobby}")

print("Nice to meet you! Let's play to my game!")

score = 0

while True:
    number = randint(0, 1)

    while True:
        user_number = int(input("Zero or One? (0/1): "))
        if user_number in [0, 1]:
            break

    if user_number == number:
        print("Yes!))")
        score += 1
    else:
        print("Nooo((")

    answer = input("One more round?;) (y - yes/n- no)")

    if answer == "n":
        print(f"Thank you for the game! Your score: {score}")
        break
    
input()
