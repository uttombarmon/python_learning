# variables
x = 1
print(x)
y = 3.2
print(y)
name = "Gabbar" 
print(name)

# multiple variables
x1,y1,z1 = 1, "game", 3
print(x1, y1, z1)

# 1 value in multiple variable assign
x2 = y2 = z2 = 3
print(x2, y2, z2)

# unpack collections

fruits =["apple", "banana", "guava"]
fruits1, fruits2, fruits3 = fruits
print(fruits1, fruits2, fruits3)

# add multiple string
first1 = "Bird "
first2 = "Can "
first3 = "Fly! "
print(first1+first2+first3)

# variable scope 
e = "true" # global variable
def myFunc():
  e = 4 # local variable
  print("Local e= ", e)
myFunc()
print("Global e= ", e)

# Illegal Variable name 
# first-name = "Mr" # Not contain any symbol except underscore(_)
# 2name = "Rahim" # Not allow number at start
# from = "Dhaka" #  Not allow use keyword as variable name

# Types Of Variable Name Declaring

myFirstName = "Mr." # Camel Case
MyLastName = "Rahim" # Pascal Case
my_address = "Dhaka" # Snake Case

print(id(my_address)) # print variable address