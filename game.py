import random

secret_number=random.randint(1,100)
attempt=0

while True:
    try:
        guess=int(input("enter your guess"))
        attempt +=1

        if guess>secret_number:
            print("number very high. Try Again")
        elif guess<secret_number:
            print("number very low. Try Again")
        else:
            print(f"Congratulations you have guessed number{secret_number} in {attempt} attempt")
    except ValueError:
        print("Plz Enter a valid integer (number)")











