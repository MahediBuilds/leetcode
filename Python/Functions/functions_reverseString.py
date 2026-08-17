def reverse_string(str):
    rev = ""
    
    i = 1
    while len(str) != len(rev):
        rev += str[-i]
        i += 1
    
    return rev

text = "hello"
