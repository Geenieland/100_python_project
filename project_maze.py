def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

        

while at_goal() != True:
    if front_is_clear() and wall_in_front() != True:
        move()
        turn_right()
   
    elif right_is_clear() and wall_in_front() != True:
        move()
        turn_left()
    else:
        turn_left()


or

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
	if right_is_clear():
		turn_right()
		move()
	elif front_is_clear():
		move()
	else:
		turn_left()
