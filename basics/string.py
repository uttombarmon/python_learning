print("Hello World!") # double qoute string
print('Hey Earth') # single qoute sting
a = "Hi, I am Barmon" # string store in variable
print(type(a)) # showing type of string asign variable

print('Hi, I am "Barmon"') # double qoute showing by qoute inside qoute
print("Hi, I am 'Barmon'") # single qoute showing by qoute inside qoute

# Multiline String
a = """
Hey, I am Barmon from Dhaka.
What is your name?
Where are you from?
""" # double qoute
b = '''
Hey, I am Barmon from Dhaka.
What is your name?
Where are you from?
''' # single qoute
print(a)
print(len(b))
print(a[1]) # string are a array which elements can access like arry elements accessing way
for x in a:
  print(x)
print("Barmon" in a) # check exit or not
print("PM" not in b) # check not exit or exit

# Slicing String
a = "Hello World!"
print(a[2:6]) # slicing from position to position
print(a[:5]) # slicing from start to position
print(a[2:]) # slicing from position to position
print(a[-5:-2]) # slicing given negative indexing

# Modifyin Strings
a = " Hello World! "
print(a.upper()) # UpperCase letters
print(a.lower()) # LowerCase letters
print(a.capitalize()) # Capitalize letters
print(a.strip()) # Remove whitespace from beggening and end
print(a.replace("H", "J")) # Replace strings
print(a.split(" ")) # Split where has whitespace

# String Concatenation
# String Concatenation Examples

# Using + operator
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Output: Hello World

# Using join() method
words = ["Hello", "World", "from", "Python"]
sentence = " ".join(words)
print(sentence)  # Output: Hello World from Python

# Using f-strings (Python 3.6+)
name = "Barmon"
age = 25
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Barmon and I am 25 years old.

# Using % formatting
name = "Barmon"
greeting = "Hello, %s!" % name
print(greeting)  # Output: Hello, Barmon!

# Using format() method
name = "Barmon"
city = "Dhaka"
intro = "I am {} from {}.".format(name, city)
print(intro)  # Output: I am Barmon from Dhaka.

# Concatenating with numbers (convert to string)
num = 42
text = "The answer is " + str(num)
print(text)  # Output: The answer is 42
