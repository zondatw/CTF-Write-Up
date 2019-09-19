import string
from collections import defaultdict

orig_table = defaultdict(list)

value = 0x04
for i in string.digits:
    orig_table[(ord(i) + value) & 0xff].append(i)

value = 0xb9
for i in string.ascii_lowercase:
    orig_table[(ord(i) + value) & 0xff].append(i)

value = 0xbf
for i in string.ascii_uppercase:
    orig_table[(ord(i) + value) & 0xff].append(i)

value = 0xbf
i = "_"
orig_table[(ord(i) + value) & 0xff].append(i)


src = 0X011E0F3A09B20C82084501AE0C8600810AA80A72010A05E601D20AC000B20707

for i in range(30, -1, -2):
    idx = (8 * i)
    target = (src >> idx) & 0xffff
    temp_orig = target & 0xf

    print(f"== {hex(target)} ==")
    for y in range(0, 4):
        orig = temp_orig + (0x10 * y)
        if ((target - orig) % 0x40) == 0:
            orig2 = (target - orig) // 0x40

            if orig in orig_table.keys() and orig2 in orig_table.keys():
                print(f"{hex(orig)} {hex(orig2)}: {orig_table[orig]} {orig_table[orig2]}")