basket = ["Apple", "Bun", "Cola"]
crate = ["Egg", "Fig", "Grape", "John's Cola"]

print("Basket List:", basket)
print("Basket Elements:", len(basket))

basket.append("Damson")
print("Appended:", basket)
print("Last item removed:", basket.pop())
print("Bucket List:", basket)

basket.extend(crate)
print("Extended:", basket)
del basket[1]
print("Item Removed:", basket)
del basket[1:3] 
# last index denotes where to stop, does not get removed
print("Slice Removed:", basket)