text = "madam"

i = 1
rev = ""

while len(text) != len(rev):
    rev += text[-i]
    i += 1
    
if rev == text:
    print("True")
else:
    print("False")