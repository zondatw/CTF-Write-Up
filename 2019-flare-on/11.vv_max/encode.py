def srld(ymm1, xmm0):
    """
    srld ymm0, ymm1, xmm0
    return ymm0
    """
    ymm0 = 0
    for i in range(7, -1, -1):
        idx = i * (8 * 4)
        temp = ymm1 >> idx & 0xffffffff
        temp = temp >> xmm0
        ymm0 |= temp << idx
    return ymm0


def cmpeqb(ymm1, ymm2):
    """
    cmpeqb ymm0, ymm1, ymm2
    return ymm0
    """
    ymm0 = 0
    for i in range(31, -1, -1):
        idx = i * 8
        temp = (ymm1 >> idx) & 0xff
        temp2 = (ymm2 >> idx) & 0xff
        if temp == temp2:
            ymm0 |= 0xff << idx
    return ymm0


def addb(ymm1, ymm2):
    """
    addb ymm0, ymm1, ymm2
    return ymm0
    """
    ymm0 = 0
    for i in range(31, -1, -1):
        idx = i * 8
        temp = (ymm1 >> idx) & 0xff
        temp2 = (ymm2 >> idx) & 0xff
        temp3 = (temp + temp2) & 0xff
        ymm0 |= temp3 << idx
    return ymm0


def shufb(ymm1, ymm2):
    """
    shufb ymm0, ymm1, ymm2
    return ymm0
    """
    ymm0 = 0
    temp_ymm2 = ymm2 & 0xffffffffffffffffffffffffffffffff
    temp_ymm1 = ymm1 & 0xffffffffffffffffffffffffffffffff
    for i in range(15, -1, -1):
        idx = i * 8
        temp2 = ((temp_ymm2 >> idx) & 0xff) % 32
        temp3 = (temp_ymm1 >> (temp2 * 8)) & 0xff
        ymm0 |= temp3 << idx

    temp_ymm2 = ymm2 >> (16 * 8)
    temp_ymm1 = ymm1 >> (16 * 8)
    for i in range(15, -1, -1):
        idx = i * 8
        temp2 = ((temp_ymm2 >> idx) & 0xff) % 32
        temp3 = (temp_ymm1 >> (temp2 * 8)) & 0xff
        ymm0 |= temp3 << (idx + (16 * 8))
    return ymm0


def addubsw(ymm1, ymm2):
    """
    addubsw ymm0, ymm1, ymm2
    return ymm0
    """
    ymm0 = 0
    for i in range(30, -1, -2):
        idx = i * 8
        idx2 = (i + 1) * 8
        temp1_1 = (ymm1 >> idx) & 0xff
        temp1_2 = (ymm2 >> idx) & 0xff
        temp2_1 = (ymm1 >> idx2) & 0xff
        temp2_2 = (ymm2 >> idx2) & 0xff
        temp1 = temp1_1 * temp1_2
        temp2 = temp2_1 * temp2_2
        ymm0 |= ((temp1 + temp2) & 0xffff) << idx
    return ymm0


def addwd(ymm1, ymm2):
    """
    addwd ymm0, ymm1, ymm2
    return ymm0
    """
    ymm0 = 0
    for i in range(14, -1, -2):
        idx = i * 16
        idx2 = (i + 1) * 16
        temp1_1 = (ymm1 >> idx) & 0xffff
        temp1_2 = (ymm2 >> idx) & 0xffff
        temp2_1 = (ymm1 >> idx2) & 0xffff
        temp2_2 = (ymm2 >> idx2) & 0xffff
        temp1 = temp1_1 * temp1_2
        temp2 = temp2_1 * temp2_2
        ymm0 |= ((temp1 + temp2) & 0xffffffff) << idx
    return ymm0


def ermb(ymm1, ymm2):
    """
    ermb ymm0, ymm1, ymm2
    return ymm0
    """
    ymm0 = 0
    for i in range(7, -1, -1):
        idx = i * (8 * 4)
        temp = (ymm1 >> idx) & 0xffffffff
        temp2 = (ymm2 >> (temp * (8 * 4))) & 0xffffffff
        ymm0 |= temp2 << idx
    return ymm0


temp_arg2 = "AABBABAB____________________??//"[::-1]
temp_arg2 = "AABBABAB____________________1234"[::-1]
temp_arg2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEF"[::-1]
#temp_arg2 = "abcdefghijklmnopqrstuvwxyzabcdef"[::-1]
#temp_arg2 = "01234567890123456789012345678901"[::-1]
#temp_arg2 = "________________________________"[::-1]
arg2 = int.from_bytes(temp_arg2.encode(), "big")

print(f"arg2: {hex(arg2)}")

a = srld(arg2, 4) # 4
print(f"#4: {hex(a)}")
a &= 0x2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f #6
print(f"#6: {hex(a)}")

b = cmpeqb(arg2, 0x2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f) #10
b = cmpeqb(arg2, 0x2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f) #15
print(f"#15: {hex(b)}")

a = addb(a, b) #23
print(f"#23: {hex(a)}")
a = shufb(0x0000000000000000b9b9bfbf041310000000000000000000b9b9bfbf04131000, a) #26
print(f"#26: {hex(a)}")

c = addb(arg2, a) # 38
print(f"#38: {hex(c)}")

a = addubsw(c, 0x0140014001400140014001400140014001400140014001400140014001400140) # 57
print(f"#57: {hex(a)}")
c = addwd(a, 0x0001100000011000000110000001100000011000000110000001100000011000) #76
print(f"#76: {hex(c)}")

c = shufb(c, 0xFFFFFFFF0C0D0E08090A040506000102FFFFFFFF0C0D0E08090A040506000102) #118
print(f"#118: {hex(c)}")
c = ermb(0xFFFFFFFFFFFFFFFF000000060000000500000004000000020000000100000000, c) #147
print(f"#147: {hex(c)}")
