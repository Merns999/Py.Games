from random import randint
import random
from re import X


# def game(n):
  
#   random_number = random.randint(1, n)
#   guess = 0
#   while guess != random_number:
#     guess = int(input(f"Enter a number from 1 to {n} : "))
#     if guess < random_number:
#       print("Sorry, that is too low")
#     elif guess > random_number:
#       print("Sorry, that is too high")
      
#   print("Accurate asf, you guessed correctly") 
  
  

# x = int(input("Set the limit: "))
# game(x)

emails = (["akidahmansur@gmail.com","abigail@gmail.com","enrique@gmail.com"])

def change(email, olddomain, newdomain):
  if "@" + olddomain in email:
    index = email.index("@" + olddomain)
    newemail = email[0:index] + newdomain
    return newemail
  return email

print(change("akidahmansur@gmail.com","gmail.com", ".co.ke"))