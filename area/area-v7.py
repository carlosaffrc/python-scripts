#!/usr/bin/python3.9
# Área de figuras geométricas
# Tratamento de erro para valor não numérico


from math import pi
import sys
import errno


def help():
    print("Entre com o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print("O valor do raio deve ser numérico")
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print("Área do círculo: ", area)
