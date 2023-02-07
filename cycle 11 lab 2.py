grades = {"Presentation": 93, "Proposal": 90, "Code": 94, "Reflection": 93,}

print(list(grades.values()))

for assignment in grades:
    print(assignment)

for assignment, grade in grades.items():
    if grade >= 70:
        print(f"{assignment}: {grade}")

for assignment, grade in grades.items():
    if grade <= 50:
        print(f"{assignment}: {grade}")