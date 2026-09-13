basket1 = {"apple", "banana", "mango", "apple", "grape"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("orange")
print("Basket 1 after adding orange:", basket1)

total_fruits = basket1.union(basket2)
print("Fruits All Together:", total_fruits)

common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets:", common_fruits)

import array as arr
fruit_counts = arr.array("i",[3, 5, 2, 4])
print("Fruit Counts array: ", fruit_counts)

fruit_counts.insert(0, 1)
fruit_counts.append(6)
print("Fruit count after adding new items: ", fruit_counts)

count_of_4 = fruit_counts.count(4)
print("Number of times four apppears", count_of_4)

fruit_counts.reverse()
print("Reversed fruit counts arrays: ", fruit_counts)