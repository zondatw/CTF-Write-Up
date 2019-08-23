# demo

## Problem
![problem](picture/problem.PNG)  

## Solution

一打開使一個A一直在旋轉:  
![init](picture/init.PNG)  

分析了很久後，發現他會create 2次 mesh，繼續觀察後發現他只會用到第一次create的，後來將第二次的資料蓋過第一個後，就噴出flag了。  

create two:
![create_two](picture/create_two.PNG)  
Call createMeshFVF:  
![create_mesh](picture/create_mesh.PNG)  
Call only one:  
![call_only_one](picture/call_only_one.PNG)  

Answer:  
![answer](picture/answer.PNG)  