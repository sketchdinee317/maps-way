y = [1, 2, 3, 4, 5, 6, 7]
print("Original list: ", y)
result = map(lambda x: x + x + x, y) 
print("\nTriple of list numbers:")
print(list(result))

