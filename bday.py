#!/usr/bin/env python

import sys
import datetime

bday = input('Please input your birth day: DD ')
bmonth = input('Please input your birth month: MM ')
byear = input('Please input your birth year: YYYY ') 
bday = datetime.datetime(int(byear), int(bmonth) , int(bday), 0, 0, 0)
now = datetime.datetime.now()
diff = now-bday
print(diff)
