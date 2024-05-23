title = "\nPython in easy steps\n"

for char in title : print(char, end = ' ')

for char in title :
	if char == 'y' :
		print("*", end = ' ')
		continue
	print(char, end = ' ')

for char in title :
	if char == 'y' :
		print("*", end = ' ')
	else :
		pass
	print(char, end = ' ')


# book just has pass after print, that's obvious...
# I added the else statement to better show the use of pass