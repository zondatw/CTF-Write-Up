# Quine

## Problem
![problem](picture/problem.PNG)  

## Solution

寫了個爆破的 script: [pass.py](./pass.py)  
主要是逐個可視字元去跑，然後用 flag 長度去決定哪個 binary 沒過直接continue，有過就變成 base_flag，接著繼續循環
