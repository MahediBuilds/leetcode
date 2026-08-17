students = {"Zain": 85, "Ahmed": 72, "Ali": 91}

name = input("Enter : ")

if name in students:
    print(students[name])
else:
    print(students.get(name, "Student not Found"))
