import random

sectert_number= random.randint(1,100)
print("Welcome To Game Of Number Guessing!!!!")

print("I have chosen a number between 1 and 100, can you guess it ?")

attempts = 0
while True:
        guess = input("Enter your guess (or type 'quit' to exit):")
        if guess.lower() == 'quit':
                print(f"You gave up! The Secret was {sectert_number}.")
                break
        try:
              guess= int(guess)
        except ValueError:
               print("Please enter a valid number.")
               continue
        attempts +=1
        if guess == sectert_number:
               print(f"Congratutions ! You guess the number in {attempts} attempts.")
               break
        elif guess < sectert_number :
            print("Too low !!! Please Try again.")
        else:
               print("Too high !! Try again.")

    