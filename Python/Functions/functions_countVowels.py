def count_vowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for ch in str:
        if ch in vowels:
            count += 1

    return count


text = "hello world"
print(count_vowels(text))
