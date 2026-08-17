def is_palindrome(text):
    rev = ""
    
    i = 1
    while len(text) != len(rev):
        rev += text[-i]
        i += 1
    
    return rev == text

