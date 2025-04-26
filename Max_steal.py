def max_steal(val):
    a = b = 0
    for v in val:
         a, b = max(b + v, a), a
    return a
val = [6, 7, 1, 3, 8, 2, 5]
print(max_steal(val)) 
