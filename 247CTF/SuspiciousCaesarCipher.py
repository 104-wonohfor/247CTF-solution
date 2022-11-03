filename = "suspicious_caesar_cipher.out"
possible_chars = "0123456789abcdef{}CTF"

# encrypt function taken from provided script
def encrypt(e, n, m):
    return [((ord(c) ** e) % n) for c in m]

# Read all the data from the provided output file (e, n, encrypted flag)
with open(filename) as f:
    content = f.readlines()

e = int(content[1])
n = int(content[2])

encrypted_data = content[4].replace("L","").replace("[","").replace("]","").replace("\n","")
encrypted_data = encrypted_data.split(', ')
enc_data = list(map(int, encrypted_data))

# Create a dictionary (translation table) by encrypting all possible characters
code_table = {}
for c in possible_chars:
    crypted = int(encrypt(e, n, c)[0])
    code_table[crypted] = c

# Check each entry in encrypted flag for corresponding char in code_table
for i in encrypted_data:
    print(code_table.get(int(i)), end = '')
