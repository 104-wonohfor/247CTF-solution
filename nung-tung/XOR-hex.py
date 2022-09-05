from itertools import cycle
import sys

def do_xor(key, message):
    message = message.replace(' ', '').decode('hex')
    key = ''.join(key.split()[::-1]).decode('hex')

    return ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, cycle(key))])

msg_file = sys.argv[1]
key = sys.argv[2]

with open(msg_file, 'rb') as f:
    message  = f.read()
f.close()

print (do_xor(key,message).encode("hex"))
