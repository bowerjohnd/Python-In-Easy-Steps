a = 1
b = 2

print("a =", a, "b =", b)

print("\nVariable a is:", "one" if (a == 1) else "not one")
print("Variable a is:", "Even" if (a % 2 == 0) else "odd")

print("\nVariable b is:", "one" if (b == 1) else "not one")
print("Variable b is:", "even" if (b % 2 == 0) else "odd")

max = a if (a > b) else b

print("\nGreater value is:", max)