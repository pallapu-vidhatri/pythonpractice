list1 = [1, 2, 3, 4, 5 ]
list2 = list1

print(list1 is list2)  # This will print True because both variables point to the same object in memory.

# Now let's create a new list with the same contents as list1

list3 = [1, 2, 3, 4, 5]

print(list1 is list3)  # This will print False because list3 is a different object in memory, even though the contents are the same.
