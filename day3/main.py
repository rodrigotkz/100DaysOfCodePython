#If/Else

print("Welcome to rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
   print("You can ride the rollercoaster!")
   age = int(input("What is your age? "))
   if age < 12:
      bill = 5
      print("Child tickets are $5.")
   elif age <= 18:
      bill = 7
      print("Youth tickets are $7.")
   elif age >= 45 and age <= 55:
      bill = 0
      print("ticket is free.")
   else:
      bill = 12
      print("Adult tickets are $12.")

   wants_photo = input("Do you want a photo taken ? Y or N.")
   if wants_photo == "Y":
      bill += 3
   
   print(f"Your final bill is ${bill}.")


else:
   print("sorry, you have to grow taller before you can ride.")

####################################################################
#IMC melhorado
height = (input("Digite a sua altura em metros: "))
weight = (input("Digite o seu peso em kg: "))

peso_int = int(weight)
altura_float = float(height)

calculo_imc = peso_int / altura_float ** 2 
imc_int = int(calculo_imc)

print(imc_int)
if imc_int < 18.5:
   print(f"O seu IMC é {imc_int}, está baixo")
elif imc_int < 25:
   print(f"O seu IMC é {imc_int}, Você tem o Imc normal.") 
elif imc_int < 30:
   print(f"O seu IMC é {imc_int}, está Alto.")
elif imc_int < 35:
   print(f"O seu IMC é {imc_int}, está Obeso")
else:
   print(f"O seu IMC é {imc_int} está muito obeso")

######################################################################
# Ano bissexto 

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print("Leap year.")
      else:
         print("Not Leap year.")
   else:
      print("leap year.")
else:
   print("Not leap year.")

#######################################################################
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2 
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e 

love_score = str(true) + str(love)
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
   print(f"Your love score is {love_score}, you go together like coke and mentos. ")
elif(love_score >= 40) and (love_score <= 50):
   print(f"Your score is {love_score}, you are alright together.")
else:
   print(f"Your score ir {love_score}")