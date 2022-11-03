from pwn import *
import re

URL="671ea6d7980a39c6.247ctf.com"  #change this   HERE YOU WILL CHANGE THE URL WHICH IS PROVIDED TO YOU FOR ATTACK
PORT=50407	#change this						   HERE YOU WILL CHANGE THE PORT NUMBER WHICH IS PROVIDED TO YOU FOR CONNECT


r = remote(URL,PORT)


print(r.recvline())

print(r.recvline())

for i in range(500):
	problem = r.recvline().decode() 	

	# print(problem)

	split = problem.split() # ['What', 'is', 'the', 'answer', 'to', '64', '+', '491']
	split2 = split[7].split('?')
	a = int(split[5])		# '64' - 64
	b = int(split2[0].strip('')) 	# '491' - 491

	

	answer = (str(a+b)+'rn').encode()
	# print(answer)
	r.sendline(answer)

	r.recvline() # b'Yes, correct!rn'


flag = r.recvline().decode().strip('rn')


print(flag)


r.close()
