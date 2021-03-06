def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        if right_is_clear():
            turn_right()
            move()
            if front_is_clear():
                move()
    elif front_is_clear():
        move()
    else:
        if wall_on_right():
            turn_left()
        else:
            turn_right()
        
