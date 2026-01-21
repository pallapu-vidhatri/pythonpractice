list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = list1

print(list1 is not list2)  # This will print True because list1 and list2 are different objects in memory.

list3 = list1

print(list1 is not list3)  # This will print False because list3 points to the same object as list1 in memory.