import os
from time import sleep

with open("ans", "wb") as f:
    pass
for _ in range(666):
    with open("ans", "a+") as f:
        f.write(" " * 69 + "\n")
    os.system("cp /mnt/hgfs/VM_share_dir/magic .")
    os.system("gdb ./magic -x script_magic.py")
    sleep(0.4)
    #os.system("./magic < ans")
