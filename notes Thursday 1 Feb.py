# -*- coding: utf-8 -*-
"""
Spyder Editor

notes Thursday 1 Feb
"""

# x and y are the function parameters
def function1(x,y):
    #these are local variables
    a=2
    b=6
    return [x+a, y+b]

output = function1(5,7)
#() -sequence
#[] - list
#{} - maps, dictionary
print(output)

#Error, since a and b are not defined
print(a)
print(b)


def function(x,y):
    #these are local variables
    a=2
    b=6
    x[5]= "goodbye
    y=2
    return [x[5] + str(a), y+b]
c={5 : "hello"}
d= {7}
output = functions1(c,d)
print(c)
print(b)
