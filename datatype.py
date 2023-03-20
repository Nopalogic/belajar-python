# data type

#integer
integer = 11
print("data: ", integer)
print("bertipe: ", type(integer))

#float
float = 3.14
print("data: ", float)
print("bertipe: ", type(float))

#string
string = "maman resing"
print("data: ", string)
print("bertipe: ", type(string))

#bool
bool = True
print("data: ", bool)
print("bertipe: ", type(bool))

#bool
bool = True
print("data: ", bool)
print("bertipe: ", type(bool))

##tipe data khusus
# komplex
komplex  = 1 + 5j
print("data: ", komplex)
print("bertipe: ", type(komplex))

# list
list  = ["asep", 32, 2.34]
print("data: ", list)
print("bertipe: ", type(list))

# tuple
tuple  = ("asep", 32, 2.34)
print("data: ", tuple)
print("bertipe: ", type(tuple))

# dictionary
dictionary  = {'id':1, 'nama':'nopal'}
print("data: ", dictionary)
print("bertipe: ", type(dictionary))

## data type from C language
from ctypes import c_double, c_char

# double
double = c_double(3.14)
print("data: ", double)
print("bertipe: ", type(double))

# char - error keneh
# char = c_char('u')
# print("data: ", char)
# print("bertipe: ", type(char))  
