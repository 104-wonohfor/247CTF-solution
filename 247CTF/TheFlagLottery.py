from pwn import *

# Set initial response to some random value
res = b'1234'

# Set up connection params
dest = "4bd5bd9cff3a0911.247ctf.com"
port = 50030

while True:
    conn = remote(dest, port)

    # Get initial message
    conn.recvline()
    # Send response
    conn.send(res)
    # Set response to current time
    res = conn.recvline()
    res = res.split()[5][:-1]

    # Print flag if we recieve it
    if conn.can_recv():
        print(conn.recvline())
        break
