# Área de figuras geométricas
# Obtendo o raio através do prompt
# Definindo uma funcão que retorna um valor


from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    raio = input("Raio do círculo: ")
    area = circulo(raio)
    print("Área do círculo: ", area)
