list1 = [1, 2, 3, 4, 5]
list2 = list1
list3 = [1, 2, 3, 4, 5]
list4 = list3

print(list1 is list2)  # This will print True because both variables point to the same object in memory.
print(list1 is list3)  # This will print False because list3 is a different
# object in memory, even though the contents are the same.
print(list3 is list4)  # This will print True because both variables point to the same object in memory.
# object in memory, even though the contents are the same.
print(list2 is list4)  # This will print False because list2 and list4 point to different objects in memory.
print(list1 is not list3)  # This will print True because list1 and list3 are different objects in memory.
print(list2 is not list4)  # This will print True because list2 and list
# point to different objects in memory.4 are different objects in memory.
print(list1 is not list2)  # This will print False because list1 and list2 point to the same object in memory.
print(list3 is not list4)  # This will print False because list3 and list4 point to the same object in memory.
