text = "aabbcdde"
textDict = dict()

for ch in text:
    textDict[ch] = textDict.get(ch, 0) + 1

for key in textDict:
    if textDict[key] == 1:
        print(key)
        break
