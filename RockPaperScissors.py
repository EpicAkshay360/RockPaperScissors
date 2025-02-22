import random

# Art for Rock, Paper, and Scissors
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices=[Rock,Paper,Scissors]

# Prompt user input
print("What do you choose?")
usr = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Validate user input
if usr not in [0, 1, 2]:
    print("Invalid choice! You must type 0, 1, or 2.")
else:
    # Generate computer choice
    cmp = random.randint(0, 2)
    
    
    # Print user choice
    print("You chose:")
    if usr == 0:
        print(Rock)
    elif usr == 1:
        print(Paper)
    elif usr == 2:
        print(Scissors)
    

    # Print computer choice
    print("Computer chose:")
    if cmp == 0:
        print(Rock)
    elif cmp == 1:
        print(Paper)
    elif cmp == 2:
        print(Scissors)
    
    # Determine winner
    if usr == cmp:
        print("It's a draw!")
    elif (usr == 0 and cmp == 2) or (usr == 1 and cmp == 0) or (usr == 2 and cmp == 1):
        print("You win!")
    else:
        print("You lose!")
