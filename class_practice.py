#!/usr/bin/env python

# use this site: http://introtopython.org/classes.html#Exercises-oop

class Rocket(object):
    # Rocket simulates a rocket ship for a game or a physics simulation.
    # Note that object is in parentheses because this is version 2.7 of Python.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket, upwards.
        self.y += 1
        
    def move_down(self):
        # Increment the y-position of the rocket, downwards.
        self.y -=1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = [Rocket() for x in range(0,5)]
for rocket in my_rockets:
    print(rocket)

# Move the first rocket up.
my_rockets[0].move_up()

# Move the second rocket down.
my_rockets[1].move_down()

# Show that only the first and second rockets have moved.
for rocket in my_rockets:
    print("Rocket altitude:", rocket.y)
    
# Exercise: Store an x and y value for a rocket.
my_rockets[1].x=12
my_rockets[1].y=53
print("Rocket 2 Coordinates:", my_rockets[1].x,my_rockets[1].y)
# Figure out how to make this more generic (i.e. The print statement should automatically call the appropirate rocket number.)

# Exercise: Store an x and y value for each rocket in a set of 5 rockets. Store these 5 rockets in a list.
from random import randint
# Note that Adam helped me with this loop:
for rocket in my_rockets:
    rocket.x=randint(0,100)
    rocket.y=randint(0,100)
    
# Make two empy lists
xcoord =[]
ycoord =[]

# Note that Adam helped me with this loop as well:
# idx is the index and it starts at 0, by default, so +1 was included for this code.
for idx, rocket in enumerate(my_rockets):
    print('Here is the location')
    print("Rocket ", idx+1 , "Coordinates:", rocket.x,rocket.y)
    xcoord.append(rocket.x)
    ycoord.append(rocket.y)
    
print(xcoord)
print(ycoord)

# This loop zips together the x and y coordinates, to show them both as a list.
for coords in zip(xcoord,ycoord):
    print(coords)
    
# Here is my original work where I did each rocket separately.
# my_rockets[1].x=randint(0,100)
# my_rockets[1].y=randint(0,100)
# print("Rocket 2 Coordinates:", my_rockets[1].x,my_rockets[1].y)
# my_rockets[2].x=randint(0,100)
# my_rockets[2].y=randint(0,100)
# print("Rocket 3 Coordinates:", my_rockets[2].x,my_rockets[2].y)
# my_rockets[3].x=randint(0,100)
# my_rockets[3].y=randint(0,100)
# print("Rocket 4 Coordinates:", my_rockets[3].x,my_rockets[3].y)
# my_rockets[4].x=randint(0,100)
# my_rockets[4].y=randint(0,100)
# print("Rocket 5 Coordinates:", my_rockets[4].x,my_rockets[4].y)


# Plot of the coordinates:
import matplotlib
matplotlib.use('Agg') #This is required to run matplotlib on Google Chrome.
import matplotlib.pyplot as plt

#x = [my_rockets[0].x, my_rockets[1].x, my_rockets[2].x, my_rockets[3].x, my_rockets[4].x]
#y = [my_rockets[0].y, my_rockets[1].y, my_rockets[2].y, my_rockets[3].y, my_rockets[4].y]
#print x
#print y

plt.scatter(xcoord,ycoord)
plt.suptitle('Rocket Coordinate Locations')
plt.xlabel('x Coordinate')
plt.ylabel('y Coordinate')
plt.show()
plt.savefig('Rocket_Coordinates.jpg', format='jpeg')