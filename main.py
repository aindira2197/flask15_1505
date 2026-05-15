students = [
    {"name": "Ali", "grade": 90},
    {"name": "Vali", "grade": 45},
    {"name": "Sami", "grade": 70},
    {"name": "Hasan", "grade": 30}
]

passed = []

for student in students:
    if student["grade"] >= 60:
        passed.append(student)

print("Otgan talabalar:")

for student in passed:
    print(student["name"], student["grade"])

print("Jami:", len(passed))
