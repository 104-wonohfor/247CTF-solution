import requests
import binascii

# Challenge URL
URL = 'https://d0967408c12f69c6.247ctf.com/'

# Specify all possible characters that could occur in flag, 247CTF{} + all hexadecimal single values a-f and 0-9
allchar = "0123456789abcdefCTF{}"

# Size of the block, we got with testing
block_size = 16

# We can predist the first 7 chars of the flag "247CTF{"
solution = '3234374354467b'

print ("Obtaining the flag from "+URL+"...")

# range is 40-len(solution) as that is the length of full flag - what we already guessed

for c in range(33):

    # Pad is 48 (3 blocks) - 1 (the char we are guessing) - how many chars have we guessed already
    # It has to be long enough so full flag can be inside.
    pad = 'AA'*(3*block_size - 1 - int(len(solution)/2))

    for i in allchar:
        x = binascii.hexlify(bytes(i, 'utf-8'))
        guess = str(x,'ascii')
        r = requests.get(URL+'/encrypt?plaintext='+pad)
        a = r.text[:96] # 96 is place on which we are guessing our byte, 3 blocks of padding + solution + guess
        r = requests.get(URL+'/encrypt?plaintext='+pad+solution+guess)
        b = r.text[:96]
        if a==b:
            print ("Found: "+i)
            solution += guess
            break

    print (binascii.unhexlify(solution).decode("utf-8"))
