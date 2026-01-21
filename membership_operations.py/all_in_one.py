numberline1 = [1, 2, 3, 4, 5]
numberline2 = numberline1
numberline3 = [1, 2, 3, 4, 5]
numberline4 = numberline3

print(numberline1 not in numberline2)  # This will print True because both variables point to the same object in memory.
print(numberline1 in numberline3)  # This will print False because numberline3

# is a different object in memory, even though the contents are the same.

print(numberline3 not in numberline4)  # This will print True because both variables point
print(numberline2 in numberline4)  # This will print False because numberline2 and numberline4 point to different objects in memory.
print(numberline2 not in numberline4)  # This will print True because numberline2 and numberline4 are different objects in memory.
