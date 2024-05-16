# simliar to an array in Java..
print("--------------------------------------------")

quarter = ["January", "February", "March"]

print("First Month:", quarter[0])
print("Second Month:", quarter[1])
print("Third Month:", quarter[2])

# each new set starts a new line, confirmed

coords = [ [1, 2, 3], [4, 5, 6] ]

print("\nTop Left 0,0:", coords[0][0])
print("Bottom Right 1,2:", coords[1][2])

print("\nSecond Month First Letter:", quarter[1][0])


print("--------------------------------------------")
# not in book, experimenting with uneven list
# book notes negative numbers start at the end of list

experiment = [ [1, 2, 3, 4, 5], [6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] ]

print("0,0:", experiment[0][0])
print("0,-5:", experiment[0][-5])
print("0,4:", experiment[0][4])
print("0,-1:", experiment[0][-1])
print("0,-6:, experiment[0][-6]) IndexError: list index out of range")

print("\n1,0:", experiment[1][0])
print("1,2:", experiment[1][2])
print("1,-1:", experiment[1][-1])
print("1,3:, experiment[1][3]) IndexError: list index out of range")

print("\n2,0:", experiment[2][0])
print("2,11:", experiment[2][11])
print("2,-1:", experiment[2][-1])
print("--------------------------------------------")
