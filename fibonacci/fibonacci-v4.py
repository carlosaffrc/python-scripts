#!/usr/bin/python3.9
# 0, 1, 2, 3, 5, 8, 13, 21...


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-1] + resultado[-2])
    return resultado


if __name__ == "__main__":
    for fib in fibonacci(10000):
        print(fib)
