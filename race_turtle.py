import random
import turtle
from race_window import RaceWindow

class RaceTurtle(turtle.Turtle):

    turtles = [] #skapar lista av turtle-objekt

    def __init__(self, w, nbr):
        super().__init__() #skapar turtle-objekt

        self._w = w #initierar w
        self._nbr = nbr #initierar nbr

        self.penup() #tar upp pennan så förflyttningen ej ritas ut
        self.goto(w.get_start_X(nbr), w.get_start_Y(nbr)) #förflyttar self (turtle) till RaceWindow-objektets start-koordinater
        self.pendown()

        self.turtles.append(self) #lägger till self i listan med turtles
    
    def race_step(self):
        self.forward(random.randint(1,6)) #går fram random steg mellan 1 och 6.
        self.xcor() #uppdaterar koordinaterna
        self.ycor() #uppdaterar koordinaterna

    def __str__(self):
        return f"Nummer {self._nbr}"
    
class MoleTurtle(RaceTurtle):

    def __init__(self, w, nbr):
        super().__init__(w, nbr)
    
    def race_step(self):
        if random.randint(0,2) == 1:
            self.penup()
        super().race_step()
        self.pendown()

    def __str__(self):
        return f"Nummer {self._nbr} - MoleTurtle"
    
class AbsentMindedTurtle(RaceTurtle):

    def __init__(self, w, nbr, tankspriddhet):
        super().__init__(w, nbr)
        self._tankspriddhet = tankspriddhet

    def race_step(self):
        if random.randint(1,100) <= self._tankspriddhet:
            pass
        else:
            super().race_step()

    def __str__(self):
        return f"Nummer {self._nbr} - AbsentMindedTurtle ({self._tankspriddhet}% Frånvarande)"
    
class DizzyTurtle(RaceTurtle):

    def __init__(self, w, nbr, yrsel):
        super().__init__(w, nbr)
        self._yrsel = yrsel

    def race_step(self):
        angle = random.randint(1,5)*self._yrsel
        if random.choice([True,False]):
            self.left(angle)
        else: 
            self.right(angle)
        super().race_step()
        self.setheading(0)

    def __str__(self):
        return f"Nummer {self._nbr} - DizzyTurtle (Yrsel: {self._yrsel})"