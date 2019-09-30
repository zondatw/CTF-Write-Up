# Overlong

## Problem
![problem](picture/problem.PNG)  

## Solution

分析一下程式  
![start](picture/start.PNG)  
發現他會解析程式內的一段編碼，剛開始只跑0x1c遍，但看題目是說Overlong，猜測可能是要多跑幾遍，因此用x32dbg將0x1c改成0x50，flag就噴出來了。  

![answer](picture/answer.PNG)  