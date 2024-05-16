chars = ['A', 'B', 'C']
#chars = ['A', 'B', 'C', 'D'] # zip() error = ValueError: zip() argument 2 is shorter than argument 1

fruit = ("Apple", "Banana", "Cherry")
dict = {'name' : "Mike", 'ref' : "Python", 'sys' : "Win"}

print("\nElements:\t", end = ' ')
for item in chars :
	print(item, end = ' ')

print("\nEnumerated:\t", end = ' ')
for item in enumerate(chars) :
	print(item, end = ' ')

print("\nZipped:\t", end = ' ')
for item in zip(chars, fruit, strict = True) :
	print(item, end = ' ')

print("\nPaired:")
for key, value in dict.items() :
	print(key, "=", value)