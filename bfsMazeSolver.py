######################################################################################################################################
##                                                                                                                                  ##
##      STUSENT NAME & MATRIC NUMBER:   NURUL HANIS BINTI MOHD DHUZUKI (1913364)                                                    ##
##                                      SAKINAH BINTI SHAMSUDDIN       (1911912)                                                    ##
##      SECTION                     :   2                                                                                           ##
##      GAME TITLE                  :   TURTLEWAY!                                                                                  ##
##      LECTURER'S NAME             :   ASSOC. PROF. TS. DR. AMELIA RITAHANI BINTI ISMAIL                                           ##
##      DESCRIPTION                 :   THIS GAME IS ABOUT FINDING THE RIGHT PATH TO REACH THE GOAL.                                ##
##                                      USER CAN ENTER ONE NUMBER BETWEEN 1 UNTIL 5 TO CHOOSE MAZE AND                              ##
##                                      THE MAZE WILL BE DISPLAYED WITH THE PATH TAKEN TO REACH GOAL.                               ##
##                                                                                                                                  ##
######################################################################################################################################

import turtle as trt                    #import turtle library
import random                           #to get random maze
import time                             #use time clock
import sys                              #import sys module
from collections import deque           #from collections module import deque(double ended queue)
import numpy as np                      #import numpy

#screen display the game
gameScreen = trt.Screen()               #define and create screen
gameScreen.bgcolor("light grey")        #put background colour
gameScreen.title("TurtleWay! Game")     #Title of the window screen
gameScreen.setup(1300,700)              #set width and height of the screen

#get input from user
def UserInput():
    userChoice = input("Please choose a number(from 1-3): ")
    return (int(userChoice) - 1);

#class for maze
class Maze(trt.Turtle):                 
    def __init__(self):                 #create function with __init__ method that known as constructor
        trt.Turtle.__init__(self)       #use self to represents the instance of the class
        self.shape("square")            #change the turtle shape to square
        self.color("black")             #set the colour of the maze to black
        self.penup()                    #to make sure the turtle move without leaving trace
        self.speed(30)                  #set the speed of the turtle

#class for the green turtle
class PathWay(trt.Turtle):              
    def __init__(self):                 #create function with __init__ method that known as constructor
        trt.Turtle.__init__(self)       #use self to represents the instance of the class
        self.shape("square")            #change the turtle shape to square
        self.color("blue")              #set the colour of the shape to blue
        self.penup()                    #to make sure the turtle move without leaving trace
        self.speed(30)                  #set the speed of the turtle

#class for the check path
class Check(trt.Turtle):                
    def __init__(self):
        trt.Turtle.__init__(self)       #use self to represents the instance of the class
        self.shape("square")            #change the turtle shape to square
        self.color("purple")            #set the colour of the shape to purple
        self.penup()                    #to make sure the turtle move without leaving trace
        self.speed(30)                  #set the speed of the turtle

#class for the start point
class StartRed(trt.Turtle):             
    def __init__(self):
        trt.Turtle.__init__(self)       #use self to represents the instance of the class
        self.shape("circle")            #change the turtle shape to circle
        self.color("red")               #set the colour of the shape to red
        self.penup()                    #to make sure the turtle move without leaving trace
        self.speed(10)                  #set the speed of the turtle

#class for the right path
class RightPath(trt.Turtle):            
    def __init__(self):
        trt.Turtle.__init__(self)       #use self to represents the instance of the class
        self.shape("turtle")            #change the turtle shape to turtle shape
        self.color("yellow")            #set the colour of the turtle to yellow
        self.penup()                    #to make sure the turtle move without leaving trace
        self.speed(10)                  #set the speed of the turtle

designMaze = np.array([
[
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+      ++ +++++++e+++     ++          ++    +++++++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+                       +  +  +              ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +                    +     +     +  +  +++  +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+     +  +     +              +              ++   +",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+  +     +  +          +   +           +  +  ++  ++",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +     +  +           +  +                 +++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+s          +                 +               ++  +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+               +                                 +",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
],
[
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+s          +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++e+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ],
[
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+s          +                 +                   +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+  +     +  +  +  + +++ + ++ ++  ++    +     +++  +",
"+  +  +  +  +  +  +  ++   ++  +  +     +  +       +",
"+  +  +  +  +     +  +++  +       ++  +  +  ++  +++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +     +++  +",
"+ ++++++ ++++++ ++++++++++++ ++ ++  +++++++++++  ++",
"+ ++  +     +++   +++   ++ +  +     +  + ++  ++  ++",
"+         +++++   ++    +  +  ++++    ++  +   +  ++",
"+ ++++++  ++    +    ++++  +  +  +++        +++  ++",
"+++++++   +++++++++        ++++  ++++++++  ++++++++",
"+     ++       +       +++                       ++",
"+  ++++  +++++++  ++++  +  ++ +  ++++++++++  ++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+    ++     +   ++     ++  +  +              ++  ++",
"++++     +         ++  +  +  +   +   ++++    ++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++  +++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++ ++++++++    + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+ ++++ ++ + +++ + +++ +++    ++    ++    ++ ++ + ++",
"+      ++ +++++++e+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
]])


def setup_maze(grid):                                   # define a function called setup_maze
    global start_x, start_y, end_x, end_y               # set up global variables for start and end locations
    for y in range(len(grid)):                          # read in the grid line by line
        for x in range(len(grid[y])):                   # read each cell in the line
            character = grid[y][x]                      # assign the varaible "character" the the x and y location of the grid
            screen_x = -588 + (x * 24)                  # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)                   # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)           # move pen to the x and y location 
                maze.stamp()                            # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))      # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))       # add " " and e to path list

            if character == "e":
                blue.color("green")
                blue.goto(screen_x, screen_y)           
                end_x, end_y = screen_x,screen_y        # assign end locations variables to end_x and end_y
                blue.stamp()
                blue.color("blue")

            if character == "s":
                start_x, start_y = screen_x, screen_y   # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


def endProgram():
    gameScreen.exitonclick()
    sys.exit()

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:                            # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()                       # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y                       # backtracking routine [cell] is the previous cell. x, y is the current cell
            purple.goto(cell)                           # identify frontier cells
            purple.stamp()
            frontier.append(cell)                       # add cell to frontier list
            visited.add((x-24, y))                      # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            purple.goto(cell)
            purple.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            purple.goto(cell)
            purple.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            purple.goto(cell)
            purple.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        blue.goto(x,y)
        blue.stamp()


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):                 # stop loop when current cells == start cell
        yellow.goto(solution[x, y])                     # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        x, y = solution[x, y]                           # "key value" now becomes the new key

# set up classes
maze = Maze()
red = StartRed()
purple = Check()
blue = PathWay()
yellow = RightPath()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                                           # dictionary to store solution path


# main program starts here #
gridchoice = UserInput()
grid = designMaze[gridchoice]
setup_maze(grid)
search(start_x,start_y)
backRoute(end_x, end_y)
gameScreen.exitonclick()

