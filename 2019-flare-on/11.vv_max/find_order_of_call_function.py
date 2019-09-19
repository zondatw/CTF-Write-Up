import re


function_table = {
    "0x00007FF7E07317B0": {
        "name": "init_data",
        "0xc00_add": 1,
    },
    "0x00007FF7E0732010": {
        "name": "move_init_data",
        "0xc00_add": 34,
    },
    "0x00007FF7E0732300": {
        "name": "addubsw",
        "0xc00_add": 4,
    },
    "0x00007FF7E07321E0": {
        "name": "addwd",
        "0xc00_add": 4,
    },
    "0x00007FF7E0733030": {
        "name": "xor",
        "0xc00_add": 4,
    },
    "0x00007FF7E0732740": {
        "name": "or",
        "0xc00_add": 4,
    },
    "0x00007FF7E0731DD0": {
        "name": "and",
        "0xc00_add": 4,
    },
    "0x00007FF7E0731CB0": {
        "name": "addb",
        "0xc00_add": 4,
    },
    "0x00007FF7E0731A70": {
        "name": "addd",
        "0xc00_add": 4,
    },
    "0x00007FF7E0732980": {
        "name": "srl",
        "0xc00_add": 4,
    },
    "0x00007FF7E07320D0": {
        "name": "sll",
        "0xc00_add": 4,
    },
    "0x00007FF7E0732A90": {
        "name": "shufb",
        "0xc00_add": 4,
    },
    "0x00007FF7E0732860": {
        "name": "split_group_and_move", # vpermd
        "0xc00_add": 4,
    },
    "0x00007FF7E0731EF0": {
        "name": "cmpeqb",
        "0xc00_add": 4,
    },
}


exclude_list = ["00007FF7E0731933"]
function_order_list = []
with open("./call_function.txt", "r") as f:
    for line in f.readlines():
        function_adr = re.search(r"\((.*)\)", line).group(1)
        if not function_adr in exclude_list:
            function_order_list.append(function_adr)

function_call_idx = 1
c00 = 0
function_current = function_order_list[0]
function_count = 1
for function_adr in function_order_list[1:]:
    if function_adr != function_current:
        function_new_adr = f"0x{function_current}"
        function_info = function_table[function_new_adr]
        c00 = (c00 + function_info["0xc00_add"]) & 0xff
        print(
            f"{function_call_idx:3} | {function_new_adr} | function name: {function_info['name']:20} | count: {function_count:3} | c00: {c00:3}"
        )
        function_call_idx += 1
        function_current = function_adr
        function_count = 1
    else:
        function_count += 1
