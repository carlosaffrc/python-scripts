#!/usr/bin/python3.9

dic = {i: i * 3 for i in range(10) if i % 2 == 0}
print(dic)

for num, triplo in dic.items():
    print(f"{num} x 3 = {triplo}")
