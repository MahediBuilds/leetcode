text = "()[]{}"

stack = []

pairs = {")": "(", "]": "[", "}": "{"}
open = "({["
close = ")}]"

valid = True

for ch in text:
    if ch in open:
        stack.append(ch)
        continue
    else:
        if len(stack) == 0:
            valid = False
            break

        if stack[-1] != pairs[ch]:
            valid = False
            break

        stack.pop()

if len(stack) != 0:
    valid = False

print(valid)
