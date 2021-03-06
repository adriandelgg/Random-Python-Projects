limit = 40
a = 1
b = 1
nearest_square = a * b

# write your while loop here
while nearest_square < limit:
    print(a * b)
    a += 1
    b += 1
    
print(nearest_square)