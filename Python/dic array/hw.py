print("Keep Track of the School Snack Count!")
menu_1 = {"Candy","Chips", "Crossaints", "Chotpoti" }
menu_2 = {"Candy", "Lolipops", "Chocolate milk", "Chips"}

print("Menus for this week: \n")
print("Menu 1: ", menu_1)
print("Menu 2: ", menu_2)

menu_1.add("Brownie")
print("After adding additional items: ", menu_1)

total_snacks = menu_1.union(menu_2)
print("Combined menu:", total_snacks)

common_snacks = menu_1.intersection(menu_2)
print("Snacks in both menus:", common_snacks)

import array as arr
menu_counts = arr.array("i",[40, 70, 80, 90])
print("Snacks price array: ", menu_counts)

menu_counts.insert(50, 100)
menu_counts.append(60)
print("Menu price after adding new items: ", menu_counts)

count_of_40 = menu_counts.count(40)
print("Number of times 40$ apppears", count_of_40)

menu_counts.reverse()
print("Reversed Menu price arrays: ", menu_counts)