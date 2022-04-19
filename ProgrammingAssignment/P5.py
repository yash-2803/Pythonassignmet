#1 exception ArithmeticError
try:
 a = 10/0
 print (a)
except ArithmeticError:
 print ("This statement is raising an arithmeticexception.")
else:
 print ("Success.")

#2 exception LookupError
try:
 a = [1, 2, 3]
 print (a[3])
except LookupError:
 print ("Index out of bound error.")


#3 exception AttributeError
class Attributes(object):
 pass
object = Attributes()
print(object.attribute)

#4 exception FloatingPointError
import math
print(math.exp(1000))

#5 exception IndexError
array = [ 0, 1, 2 ]
print (array[3])
