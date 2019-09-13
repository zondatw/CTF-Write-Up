
edi = 0x38464947
ebx = 0x02c16139
esi = 0
key = "AAAAAAAA"
count = 0x20

for i in range(count):
    edx = ((ord(key[esi & 3]) & 0xff) + esi) & 0xffffffff
    print(f"edx: {hex(edx)}")
    esi = ((esi - 0x61c88647) + 0x100000000) & 0xffffffff
    print(f"esi: {hex(esi)}")
    edi = (((((ebx << 4) ^ (ebx >> 5)) + ebx) ^ edx) + edi) & 0xffffffff
    print(f"edi: {hex(edi)}")
    print(f"edi << 4: {hex(edi << 4)}")
    print(f"edi >> 5: {hex(edi >> 5)}")
    print(f"(edi << 4) ^ (edi >> 5): {hex((edi << 4) ^ (edi >> 5))}")
    ecx = (((edi << 4) ^ (edi >> 5)) + edi) & 0xffffffff
    print(f"ecx: {hex(ecx)}")
    ecx = (((ord(key[(esi >> 0xb) & 3]) & 0xff) + esi) ^ ecx) & 0xffffffff
    print(f"ecx: {hex(ecx)}")
    ebx = (ebx + ecx) & 0xffffffff

    print(f"gif 1: {hex(edi)}")
    print(f"gif 2: {hex(ebx)}")
    print("=" * 35)