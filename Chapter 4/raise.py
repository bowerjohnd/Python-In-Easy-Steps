day = 32

try :
	if day > 31 :
		raise ValueError("Invalid Day Number")
	# More statements to execute get added here.

except ValueError as msg :
	print("The program found an", msg)

finally :
	print("But Today Is Beautiful Anyway.")