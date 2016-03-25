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
print c.name # if only put c.name, it doesn't print 'Jennifer' to the screen, but if put print c.name, it does

c.name = 'Adam' 
print c.name # prints Adam; note that we were able to overwrite using this object oriented programming.



# Let's create another variable within our class.

class Chat2:
    name2 = 'Jennifer2'
    def insert2(self2):
        print 'We inserted something.'
    def delete2(self2):
        print 'We deleted something.'
    def change2(self2,value2):
        self2.name2 = value2

c2 = Chat2()
print c2 # <__main__.Chat2 instance at 0x7f77b696edd0>
print c2.name2 # prints 'Jennifer2'
print c2.change2('Adam2') # prints 'None', but then:
print c2.name2 # prints 'Adam2'

# This allows us to manipulate values!  Cool!



