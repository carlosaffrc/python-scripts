#!/usr/bin/python3.9
# 0, 1, 2, 3, 5, 8, 13, 21...


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == "__main__":
    # Lista of 15 primeiros numeros da sequência
    for fib in fibonacci(10000):
        print(fib)
