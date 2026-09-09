tuplex = ("exercise", "read", "drink water")
print("Habits (initial):", tuplex)

tuple1 = ("hair care",)
tuplex = tuplex + tuple1
#tuplex = tuplex + ("hair care",) 
print("Habits (updated):", tuplex)

slice1 = tuplex[0:2]  
slice2 = tuplex[2:]  

print("First 2 Habits:", slice1)
print("Remaining Habits:", slice2)

print(tuplex[0])
print(tuplex[1])
print(tuplex[3])

