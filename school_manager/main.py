# import a module
import school

# import a whole package
#from school import *

print("hello world")
print(school.SCHOOL_NAME)
#ram = school.Student('Ram Singh', 1, 5)

#method 2: import individual item from the module
from school import SCHOOL_NAME

print(SCHOOL_NAME)

"""
method 2b: without using 'from' keyworkd
import school.Student

print(SCHOOL_NAME)
"""

#importing multiple items
from school import ClassRoom, ring_bell, \
    SCHOOL_NAME



#import as tuple
# when multiple items are needed to used
from school import (ClassRoom, 
                    ring_bell, 
                    SCHOOL_NAME
                    )

#x = 5
x = \
    5
print(x)

