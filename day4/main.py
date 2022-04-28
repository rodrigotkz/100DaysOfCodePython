import random


random_integer = random.randint(1,2)

if random_integer == 1:
   print("Deu cara!")
else: 
   print("Deu coroa!")

##############################################################

states_of_america = ["Delaware", "Pennsylvania", "Virginia"]
states_of_america[1] = "São Paulo"  
states_of_america.append("Rio de janeiro")

print(states_of_america)

###############################################################

import random 
 Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)

random_choice = random.randint(0, num_items -1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

##################################################################

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",]
vegetables = ["Sppinach", "Kale", "Tomatoes","Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

################################################################

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

###############################################################
# 🚨 Don't change the code below 👇
from tkinter import HORIZONTAL


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")