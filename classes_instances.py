#!/usr/bin/env python

# Here we will run through a couple tutorials for object oriented programming, specifically classes, instances (objects), attributes, and methods

# https://www.youtube.com/watch?v=VuaRZhROqPg
# https://www.youtube.com/watch?v=CtzVNCmysFs

var = 'Hello World!' #var is a string, so it is a string object
print type(var)
print var.upper() #prints the variable in all upper case letters

# Here is some example code, but it doesn't work right now.  It needs to be fixed.
'''class Car(object):
redcar = Car('red') #Car is the class, and here we are passing a color value
bluecar = Car('blue') 

redcar.start()
redcar.openleft()
redcar.start()

bluecar.start()

redcar.stop()'''

class Chat:
    name = 'Jennifer'
    def insert(self):
        print 'We inserted something.'
    def delete(self):
        print 'We deleted something.'
        
c = Chat()
print c # <__main__.Chat instance at 0x7fcc0976ea70> # Notice this value compared to the one below for d -- even though Chat() is the same thing, it is used for a different instance between c and d.
d = Chat()
print d # <__main__.Chat instance at 0x7fcc0976eb00>

c.insert() # prints 'We inserted something.' # Use the dot notation to go into objects.  Here the c is the instance and the insert is the method.
c.delete() # prints 'We deleted something.'
c.name # should print 'Jennifer' but for some reason this isn't working.  I'm not sure what I'm doing wrong here.


