#!/usr/bin/env python

# Here we will run through a couple tutorials for object oriented programming, specifically classes, instances (objects), attributes, and methods

# https://www.youtube.com/watch?v=VuaRZhROqPg
# https://www.youtube.com/watch?v=CtzVNCmysFs

var = 'Hello World!' #var is a string, so it is a string object
print type(var)
print var.upper() #prints the variable in all upper case letters

class Car(object):
redcar = Car('red') #Car is the class, and here we are passing a color value
bluecar = Car('blue') 

redcar.start()
redcar.openleft()
redcar.start()

bluecar.start()

redcar.stop()
