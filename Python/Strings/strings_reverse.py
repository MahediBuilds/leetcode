text = "hello"

rev_text = ""
i = 1

while len(text) != len(rev_text):
    rev_text += text[-i]
    i += 1
    
print(rev_text)