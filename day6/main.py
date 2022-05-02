#Reeborgs world1
#Link https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

#Reeborg Worlds Hurdle2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def xiter():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    xiter()

#Reeborg Worlds Hurdle2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def xiter():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    xiter()
    

#Reeborg Wordl Hurdle3

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def xiter():
    turn_left()
    move()   
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        xiter()
    else:
        move()

#Reboorg Wordls Hurdles4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def xiter():
    turn_left()
    while wall_on_right():
        move()        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()    
    turn_left()    
    
while not at_goal():
    if wall_in_front():
        xiter()
    else:
        move()