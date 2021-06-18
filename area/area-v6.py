#!/usr/bin/python3.9
# Área de figuras geométricas
# Implementando uma funcão help()
# Tratamento de erro para número insuficiente
# de parâmetros na linha de comando


from math import pi
import sys


def help():
    print("Entre com o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print("Área do círculo: ", area)
