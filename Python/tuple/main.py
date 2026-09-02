tuplex = ("tuple", 3.2, False, 1)
print(tuplex)

tuple = (4, 6, 2, 8, 3, 1)
print(tuplex)

tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
# use + to add to tupple and create new tuple cuz tuples are immutable

tuplex = tuplex + (9,)
print(tuplex)

tuple1 = ( 50, 10, 60, 70, 50)
print(tuple1.count(50))

# tuple[start:stop] start and stop index
tuple = (2, 3, 4, 5, 6, 7, 8, 6, 1)
_slice = tuple[3:5]
print(_slice)
_slice = tuple[:6]
print(_slice)