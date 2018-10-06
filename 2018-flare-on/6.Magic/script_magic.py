import gdb
from functools import wraps
import string

def print_func_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(" {} ".format(func.__name__).center(20, '='))
        ret = func(*args, **kwargs)
        print(" |{}| ".format(ret).center(20, '='))
        gdb.execute('printf "%s", {}'.format(user_input_ptr))
        return ret
    return wrapper

def get_fibonacci_table():
    fibonacci_table = {}
    a, b, c = 0, 1, 0
    for i in range(0x100):
        a = (b + c) % 0x10000000000000000
        c = b
        b = a
        fibonacci_table[a] = i + 1
    return fibonacci_table

def get_func2_table():
    func2_table = {}
    for i in range(0x100):
        xor_num = 0xffffffff
        user_input = i
        xor_num ^= user_input
        for _ in range(8):
            b = -(xor_num & 1)
            xor_num = ((b & 0xedb88320) ^ (xor_num >> 1)) % 0x100000000
        func2_table[0xffffffff - xor_num] = i
    return func2_table

def resolve_func2(xor_num):
    xor_num = 0xffffffff - xor_num
    xor_dict = {
        1: 0xedb88320,
        0: 0,
    }

    bit = 0
    last_xor_num = 0x0
    for i in range(8):
        last_bit = (xor_num >> 31) & 0x1
        xor_num ^= xor_dict[last_bit]
        xor_num = (xor_num << 1) | last_bit
        bit = (bit << 1) | (xor_num & 1)
        if (last_bit == 1 and i == 6):
            last_xor_num |= 0x80
        if (last_bit == 1 and i == 7):
            last_xor_num |= 0x40
    return bit ^ last_xor_num ^ 0xff

def brute_force_func2(xor_num, length, target):
    if length == 0:
        return []
    for i in string.printable:
        temp_xor_num = xor_num ^ ord(i)
        for _ in range(8):
            b = -(temp_xor_num & 1)
            temp_xor_num = ((b & 0xedb88320) ^ (temp_xor_num >> 1)) % 0x100000000
        if (0xffffffff - temp_xor_num) == target:
            return [ord(i)]
        ret = brute_force_func2(temp_xor_num, length - 1, target)
        if ret:
            r = [ord(i)]
            r.extend(ret)
            return r
    return []


def get_func4_table_str():
    func4_table_str = b''
    with open("func4_table", "rb") as f:
        byte = f.read(1)
        while byte != b"":
            func4_table_str += byte
            byte = f.read(1)
    return func4_table_str

fibonacci_table = get_fibonacci_table()
func2_table = get_func2_table()
func4_table_str = get_func4_table_str()

def until(address_list):
    while True:
        gdb.execute("s")
        rip = gdb.parse_and_eval("$rip")
        if rip in address_list:
            break
    return rip

def bypass_fibonacci_func(user_input, fibonacci_table, call_func_fin):
    ans = ''
    count = 0
    while True:
        gdb.execute("c")
        addr = gdb.parse_and_eval("$rip")
        if addr == call_func_fin:
            break
        rax = gdb.parse_and_eval("$rax")
        word = fibonacci_table[int(rax) % 0x10000000000000000]
        gdb.execute("set {type}({user_input} + {count}) = {word}".format(
            type="{byte}", user_input=user_input, count=count, word=hex(word)))
        ans += chr(word)
        gdb.execute("set $rdx = {}".format(rax))
        count += 1
    return ans

@print_func_name
def bypass_func_1(call_func_fin):
    ans = ''
    gdb.execute("n")
    func_base = gdb.parse_and_eval("$rip")
    user_input = gdb.parse_and_eval("$rdi")
    cmp_addr = func_base + 0x124
    gdb.execute("b *{}".format(cmp_addr))
    temp = bypass_fibonacci_func(user_input, fibonacci_table, call_func_fin)
    ans += temp
    gdb.execute("c")
    return ans

@print_func_name
def bypass_func_2():
    ans = ''
    gdb.execute("n")
    rdx_ptr_value = gdb.parse_and_eval("*$rdx")
    user_input = gdb.parse_and_eval("$rdi")
    length = int(gdb.parse_and_eval("$rsi"))
    if length == 1:
        words = [resolve_func2(int(rdx_ptr_value))]
    else:
        words = brute_force_func2(0xffffffff, length, int(0x100000000 + rdx_ptr_value)) 
    for count, word in enumerate(words):
        gdb.execute("set {type}({user_input} + {count}) = {word}".format(
            type="{byte}", user_input=user_input, count=count, word=hex(word)))
        ans += chr(word)
    gdb.execute("c")
    gdb.execute("c")
    return ans

@print_func_name
def bypass_func_3(call_func_fin):
    ans = ''
    gdb.execute("n")
    func_base = gdb.parse_and_eval("$rip")
    user_input = gdb.parse_and_eval("$rdi")
    cmp_addr = func_base + 0x2d7
    gdb.execute("b *{}".format(cmp_addr))
    count = 0
    while True:
        gdb.execute("c")
        addr = gdb.parse_and_eval("$rip")
        if addr == call_func_fin:
            break
        buf_val = int(gdb.parse_and_eval("$al"))
        func_call_val = int(gdb.parse_and_eval("$dl"))
        word = (buf_val ^ func_call_val) % 0x100
        gdb.execute("set {type}({user_input} + {count}) = {word}".format(
            type="{byte}", user_input=user_input, count=count, word=hex(word)))
        gdb.execute("set $rcx = {}".format(hex(word)))
        ans += chr(word)
        count += 1
    gdb.execute("c")
    return ans

@print_func_name
def bypass_func_4(call_func_fin, func4_table_stri):
    ans = ''
    gdb.execute("n")
    func_base = gdb.parse_and_eval("$rip")
    user_input = gdb.parse_and_eval("$rdi")
    length = gdb.parse_and_eval("$rsi")
    
    cmp_addr = func_base + 0x143
    gdb.execute("b *{}".format(cmp_addr))

    cmp1_addr = func_base + 0x1EC
    gdb.execute("b *{}".format(cmp1_addr))
    
    cmp2_1_addr = func_base + 0x286
    gdb.execute("b *{}".format(cmp2_1_addr))
    cmp2_2_addr = func_base + 0x2F8
    gdb.execute("b *{}".format(cmp2_2_addr))

    word = 0
    count = -1
    while True:
        if count != (length-1):
            count += 1
        gdb.execute("c")
        rip = gdb.parse_and_eval("$rip")
        if rip == call_func_fin:
            break
        cmp_value = gdb.parse_and_eval("$dl")
        tb_idx = func4_table_str.index(chr(int(cmp_value))) 
        gdb.execute("set $rax = {}".format(hex(tb_idx)))
        if rip == cmp_addr:
            print('cmp_addr')
            word = (tb_idx << 2) | (word & 0x3)
            word_temp = (tb_idx << 2) | (word & 0x3)
            gdb.execute("set {type}({user_input} + {count}) = {word}".format(
                type="{byte}", user_input=user_input, count=count//2, word=hex(word_temp)))
    
        elif rip == cmp1_addr: 
            print('cmp1_addr')
            word = (word & 0xfc) | ((tb_idx >> 4) & 0x3)
            word_temp = word
            gdb.execute("set {type}({user_input} + {count}) = {word}".format(
                type="{byte}", user_input=user_input, count=(count//2), word=hex(word_temp)))
            ans += chr(word_temp)
            word_temp = tb_idx & 0xf

        elif rip == cmp2_1_addr:
            print('cmp2_1_addr')
            word = ((word << 4) | (tb_idx >> 2)) & 0xff
            word_temp = word
            gdb.execute("set {type}({user_input} + {count}) = {word}".format(
                type="{byte}", user_input=user_input, count=count//2, word=hex(word_temp)))
            word_temp = tb_idx & 0x3
            

        elif rip == cmp2_2_addr:
            print('cmp2_2_addr')
            word = (word << 6) | (tb_idx & 0x3f) 
            word_temp = word
            gdb.execute("set {type}({user_input} + {count}) = {word}".format(
               type="{byte}", user_input=user_input, count=(count//2) + 1, word=hex(word_temp)))
            ans += chr(word_temp)
        word = word_temp
    gdb.execute("c")
    return ans

@print_func_name
def bypass_func_5(call_func_fin):
    ans = ''
    gdb.execute("n")
    func_base = gdb.parse_and_eval("$rip")
    user_input = gdb.parse_and_eval("$rdi")
    cmp_addr = func_base + 0x71
    gdb.execute("b *{}".format(cmp_addr))
    count = 0
    while True:
        gdb.execute("c")
        addr = gdb.parse_and_eval("$rip")
        if addr == call_func_fin:
            break
        cmp_value = int(gdb.parse_and_eval("$al")) % 0x100
        word = cmp_value - 13
        gdb.execute("set {type}({user_input} + {count}) = {word}".format(
            type="{byte}", user_input=user_input, count=count, word=hex(word)))
        gdb.execute("set $ecx = {}".format(hex(cmp_value)))
        ans += chr(word)
        count += 1
    gdb.execute("c")
    return ans

@print_func_name
def bypass_func_6(call_func_fin):
    ans = ''
    gdb.execute("n")
    func_base = gdb.parse_and_eval("$rip")
    user_input = gdb.parse_and_eval("$rdi")
    cmp_addr = func_base + 0x5e
    gdb.execute("b *{}".format(cmp_addr))
    count = 0
    while True:
        gdb.execute("c")
        addr = gdb.parse_and_eval("$rip")
        if addr == call_func_fin:
            break
        word = int(gdb.parse_and_eval("$al")) % 0x100
        gdb.execute("set {type}({user_input} + {count}) = {word}".format(
            type="{byte}", user_input=user_input, count=count, word=hex(word)))
        gdb.execute("set $edx = {}".format(hex(word)))
        ans += chr(word)
        count += 1
    gdb.execute("c")
    return ans

@print_func_name
def bypass_func_7(call_func_fin):
    ans = ''
    gdb.execute("n")
    func_base = gdb.parse_and_eval("$rip")
    user_input = gdb.parse_and_eval("$rdi")
    cmp_addr = func_base + 0x66
    gdb.execute("b *{}".format(cmp_addr))
    count = 0
    while True:
        gdb.execute("c")
        addr = gdb.parse_and_eval("$rip")
        if addr == call_func_fin:
            break
        cmp_value = int(gdb.parse_and_eval("$al")) % 0x100
        word = cmp_value ^ 0x2a
        gdb.execute("set {type}({user_input} + {count}) = {word}".format(
            type="{byte}", user_input=user_input, count=count, word=hex(word)))
        gdb.execute("set $ecx = {}".format(hex(cmp_value)))
        ans += chr(word)
        count += 1
    gdb.execute("c")
    return ans


call_xor_func = 0x402E8A
call_key_func = 0x403B5D
call_func = 0x402f06
call_func_fin = 0x402f08
key_func_fin = 0x403b62
#x_func = 0x4037bf
x_func_fin = 0x403BCC

gdb.execute("start < ans")

#gdb.execute("b *{}".format(hex(call_xor_func)))
gdb.execute("b *{}".format(hex(call_key_func)))

with open("ans", "r") as f:
    length = len(f.readlines())
for i in range(length):
    gdb.execute("c")

gdb.execute("b *{}".format(hex(call_func)))
gdb.execute("b *{}".format(hex(call_func_fin)))
gdb.execute("b *{}".format(hex(key_func_fin)))
#gdb.execute("b *{}".format(hex(x_func)))
#gdb.execute("b *{}".format(hex(x_func_fin)))

#gdb.execute("c")
# input
user_input_ptr = gdb.parse_and_eval("$rdi")
gdb.execute('printf "%s", {}'.format(user_input_ptr))
gdb.execute("c")

for i in range(1, 33+1):
    print(" {} ".format(i).center(20, "="))
    func_part = int(gdb.parse_and_eval('(0x100000000+*($rcx+0x14))')) % 0x100000000

    if func_part == 0x19e90000:
        bypass_func_1(call_func_fin)
    elif func_part == 0x0000fc45:
        bypass_func_2()
    elif func_part == 0xfffffec4:
        bypass_func_3(call_func_fin)
    elif func_part == 0x46a7c264:
        bypass_func_4(call_func_fin, func4_table_str)
    elif func_part == 0x45c70000:
        bypass_func_5(call_func_fin)
    elif func_part == 0x55eb0000:
        bypass_func_6(call_func_fin)
    elif func_part == 0x5deb0000:
        bypass_func_7(call_func_fin)

i = gdb.inferiors()[0]
m = i.read_memory(int(user_input_ptr), 69) + "\n"
with open("ans", "r+") as f:
    ans = f.readlines()
    ans[-1] = m
    f.seek(0)
    f.truncate()
    f.seek(0)
    f.writelines(ans)
with open("input", "w") as f:
    f.write(m)
gdb.execute("q")
