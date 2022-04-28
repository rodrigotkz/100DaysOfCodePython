print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

start = input("Vamos começar? escolha seu caminho!!seguir direita ou esquerda? ")
start_lower = start.lower()

if start == "esquerda": 
  fase2 = input("Você chegou a floresta perdida! seguir para direita ou esquerda? ")
  fase2_lower = fase2.lower()
else:
  print("Você morreu!! acabou pisando em falso e caiu do barranco. F")
  
if fase2 == "esquerda": 
  fase3 = input("Você encontrou a caverna secreta! entrar ou desviar dela? ")
  fase3_lower = fase3.lower()
else:
  print("Você morreu!!! infelizmente deu de cara com uma tribo índigena canibais.")
  
if fase3 == "entrar": 
  fase4 = input("Você entrou na caverna dos mortos!! seguir direita ou esquerda?  ")
  fase4_lower = fase4.lower()
else:
  print("Você morreu!! infelizmente deu de cara com um Urso faminto!.")
  
if fase4 == "direita":
  print("Você chegou ao tesouro!! Parabéns você venceu.")
else: 
  print("Você caiu em uma armadilha e morreu! GAME OVER.")