students = {"Zain": 85, "Ahmed": 72, "Ali": 91}

name = input("Enter : ")

for keys in students:
    if name.lower() == keys.lower():
        found = True
        break
    else:
        found = False

if found:
    print("Found")
else:
    print("Not Found")
