from race_turtle import RaceTurtle
from race_window import RaceWindow
import random
from race_turtle import MoleTurtle
from race_turtle import AbsentMindedTurtle
from race_turtle import DizzyTurtle

class TurtleRace:

    w = RaceWindow()
    start_list = []
    for i in range(1,9):
        t = random.randint(1,3)
        if t == 1:
            start_list.append(MoleTurtle(w, i))
        elif t == 2: 
            start_list.append(AbsentMindedTurtle(w, i, random.randint(0,100)))
        else:
            start_list.append(DizzyTurtle(w, i, random.randint(1,5)))
    
    end_list = []
    for i in range(8):
        print(start_list[i])
    
    while len(start_list) > 0:
        for turtle in start_list:
            if turtle.ycor() >= 200:
                turtle.setheading(-45)
            elif turtle.ycor() <= -200:
                turtle.setheading(45)
            turtle.race_step()
            if turtle.xcor() >= w.X_END_POS:
                end_list.append(turtle)
                start_list.remove(turtle)
        
    for i in range(3):
        print(f"På plats {i+1}: {end_list[i]}")


'''
    for i in range(1,9):
        start_list.append(RaceTurtle(w,i))

    end_list = []

    while len(start_list) > 0:
        for turtle in start_list:
            turtle.race_step()
            if turtle.xcor() >= w.X_END_POS:
                end_list.append(turtle)
                start_list.remove(turtle)
        
    for i in range(3):
        print(f"På plats {i+1}: {end_list[i]}")
'''