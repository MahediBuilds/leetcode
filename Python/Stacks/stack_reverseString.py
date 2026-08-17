text = "hello"

textStack = list(text)
rev = ""

i = 0
while i != len(textStack):
    rev += textStack.pop()

print(rev)
