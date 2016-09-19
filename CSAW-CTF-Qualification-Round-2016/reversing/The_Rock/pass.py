
check = bytearray('FLAG23456912365453475897834567')

s = bytearray('012345678901234567890123456789')

for i in xrange(len(check)):
    check[i] = (((check[i] - 9) ^ 0x10) - 20) ^ 0x50

print check

'''
for i in xrange(len(s)):
    s[i] = (s[i] ^ 0x50) + 20

print s

for i in xrange(len(s)):
    s[i] = (s[i] ^ 0x10) + 9

print s
'''

