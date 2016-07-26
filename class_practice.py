#!/usr/bin/env python
# use this site: http://introtopython.org/classes.html#Exercises-oop

class Rocket(object):
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    # Note that object is in parentheses because this is version 2.7 of Python.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = [Rocket() for x in range(0,5)]

# Move the first rocket up.
my_rockets[0].move_up()

# Show that only the first rocket has moved.
for rocket in my_rockets:
    print("Rocket altitude:", rocket.y)
    
# Exercise: Store an x and y value for a rocket.
my_rockets[1].x=12
my_rockets[1].y=53
print("Rocket 2 Coordinates:", my_rockets[1].x,my_rockets[1].y)
# Figure out how to make this more generic (i.e. The print statement should automatically call the appropirate rocket number.)

# Exercise: Store an x and y value for each rocket in a set of 5 rockets. Store these 5 rockets in a list.
from random import randint
my_rockets[0].x=randint(0,100)
my_rockets[0].y=randint(0,100)
print("Rocket 1 Coordinates:", my_rockets[0].x,my_rockets[0].y)
my_rockets[1].x=randint(0,100)
my_rockets[1].y=randint(0,100)
print("Rocket 2 Coordinates:", my_rockets[1].x,my_rockets[1].y)
my_rockets[2].x=randint(0,100)
my_rockets[2].y=randint(0,100)
print("Rocket 3 Coordinates:", my_rockets[2].x,my_rockets[2].y)
my_rockets[3].x=randint(0,100)
my_rockets[3].y=randint(0,100)
print("Rocket 4 Coordinates:", my_rockets[3].x,my_rockets[3].y)
my_rockets[4].x=randint(0,100)
my_rockets[4].y=randint(0,100)
print("Rocket 5 Coordinates:", my_rockets[4].x,my_rockets[4].y)

# List of all coordinates:
#all_coordinates = [Rocket() for x in range(0,5)]
#for i in all_coordinates:
#   print "Coordinates %str" % i

# Figure out how to do the above lines of code as a loop.  This is messy as is.
# Plot of the coordinates:
import matplotlib
matplotlib.use('Agg') #This is required to run matplotlib on Google Chrome.
import matplotlib.pyplot as plt
x = [my_rockets[0].x, my_rockets[1].x, my_rockets[2].x, my_rockets[3].x, my_rockets[4].x]
y = [my_rockets[0].y, my_rockets[1].y, my_rockets[2].y, my_rockets[3].y, my_rockets[4].y]
plt.scatter(x,y)
plt.suptitle('Rocket Coordinate Locations')
plt.xlabel('x Coordinate')
plt.ylabel('y Coordinate')
plt.savefig('Rocket_Coordinates')