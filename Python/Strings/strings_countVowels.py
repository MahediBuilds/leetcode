text = "hello world"

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for ch in text:
    if ch in vowels:
        count += 1
        
print(count)