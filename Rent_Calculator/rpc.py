''' 
User choice - rock paper scissor 
Computer choice - rock paper scissor
evaluate winner
display output
'''

import random
choices = ["rock", "paper", "scissor"]
user = input("Enter your move")
computer = random.choice(choices)

print(f"User choice is {user} & Computer choice is {computer}")

