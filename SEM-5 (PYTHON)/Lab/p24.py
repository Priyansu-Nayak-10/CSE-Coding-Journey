numbers=list(range(1,6))
key=11
if key in numbers:
	print(f"The index of {key} is {numbers.index(key)}")
else:
	print("Index not found.")
