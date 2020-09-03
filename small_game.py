# This is a guessing nubmer game

# We try to apply method inside the python libaray to run our game
import random

# We want to create a random nubmer
lucky_number=random.randint(1,10)

# We also want to create a loop, so you can determine how many chance you have
for i in range(0,3):

    # the user have to Enter their nubmer
    my_nubmer=int(input("Enter a number \n"))
    # we gona print out "Enter a nuber to the terminal below,"
    # the program will wait untile we enter a number 


# We also want to determine whether the user guess successfully or not
    if my_nubmer == lucky_number:
        print("Are you living inside my brain? ")
        print("\n")
        break
        # Onece the guessing is correct, we will end the loop by using break

    if my_nubmer < lucky_number:
        print("Nope, too small")
        print("\n")
        continue
    # Once the user didn't get the number, he/she might use the second chance 

    if my_nubmer > lucky_number:
        print("Nope, too big")
        print("\n")
        continue
    # Once the user didn't get the number, he/she might use the second chance 
# don't forget the TAPs above.
else:
    print("The answer is "+str(lucky_number)+" hahahahah")


