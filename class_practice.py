#!/usr/bin/env python

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
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