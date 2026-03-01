# Data Type Check
# Text Type:	str

# Numeric Types:	int, float, complex
x = 2  # Numeric: Integer
# print(type(x))
y = 2.3 # Numeric: Float
# print(type(y))
z = 2j # Numeric:Complex
# print(type(z))

# Sequence Types:	list, tuple, range
x = ["Game1", "Game1", "Game1"] # List
print(type(x))

y = ("apple", "banana", "cherry") # Tuple
print(type(y))

# Mapping Type:	dict
z = { "name": "Demo", "Profession" : "Doctor", "age": 34} # Dictionary
print(type(z))

# Set Types:	set, frozenset
s = {"Habib", "Mosh", "Khabim"} # Set
print(type(s))

# Boolean Type:	bool
isHuman = True
# Binary Types:	bytes, bytearray, memoryview
c = b"Hello" # bytes
print(type(c))
print(c)

b = bytearray(4) # bytearray
print(type(b))
print(b)

d = memoryview(bytes(4)) # memoryview
print(type(d))
print(d)
