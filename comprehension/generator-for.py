#!/usr/bin/python3.9

generator = (i * 3 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
