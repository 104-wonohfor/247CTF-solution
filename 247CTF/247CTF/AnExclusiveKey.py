import string

key = "247CTF{"
keyspace = string.hexdigits[:16]

with open("exclusive_key", "rb") as f:
    xorfile = f.read()

score = {' ':27, '<':27, '>':27, '/':27, 'e':26, 't':25, 'a':24, 'o':23, 'i':22, 'n':21, 's':20, 'h':19, 'r':18, 'd':17, 'l':16, 'c':15, 'u':14, 'm':13, 'w':12, 'f':11, 'g':10, 'y':9, 'p':8, 'b':7, 'v':6, 'k':5, 'j':4, 'x':3, 'q':2, 'z':1}

def scoreText(text):
    total = 0
    for c in text:
        if c.lower() in score:
            total += score[c.lower()]
        else:
            total -= 1
    return total

def xorText(ciphertext, key):
    result = ""
    for index, char in enumerate(ciphertext):
        result += chr(char ^ ord(key[index % len(key)]))
    return result

# We know the last char is "}"
while len(key) < 39:
    highScore = 0
    for char in keyspace:
        tempKey = key + char + "0" * (38 - len(key)) + "}"
        text = xorText(xorfile, tempKey)
        tempScore = scoreText(text)
        if tempScore > highScore:
            highScore = tempScore
            highScoreChar = char
    key += highScoreChar
    print(key)
    
key += "}"

print(xorText(xorfile, key))
print(key)
