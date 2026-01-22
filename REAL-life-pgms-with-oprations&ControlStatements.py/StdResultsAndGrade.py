maraks = float(input("Enter the marks obtained: "))

if maraks >= 90:
    grade = 'A'
elif maraks >= 75:
    grade = 'B'
elif maraks >= 50:
    grade = 'C'
elif maraks >= 35:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)
