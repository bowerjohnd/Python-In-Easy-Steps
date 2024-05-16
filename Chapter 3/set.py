zoo = ("Kangaroo", "Leopard", "Moose")
print("Typle:", zoo, "\tLength:", len(zoo))
print(type(zoo))

#bag = frozenset({"Red", "Green", "Blue"})	# immutable set
bag = {"Red", "Green", "Blue"}
bag.add("Yellow")
bag.add("Red")					# testing only unique allowed, true
print("\nSet:", bag, "\tLength:", len(bag))
print(type(bag))

print("\nIs Green in the bag set?:", "Green" in bag)
print("Is Orange in the bag set?:", "Orange" in bag)

box = {"Red", "Purple", "Yellow"}
print("\nSet:", box, "\t\tLength:", len(box))
print("Common to both sets:", bag.intersection(box))