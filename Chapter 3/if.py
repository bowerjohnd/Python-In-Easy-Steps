num = int( input("Please enter a number: ") )

if num > 5 :
	print("Number exceeds 5\n")
elif num < 5 :
	print("Number is less than 5\n")
else :
	print("Number is 5\n")

cmd = input("Enter STOP or GO: ").upper()

match cmd :
	case "GO":
		print("Started...")
	case "STOP":
		print("Halted!")