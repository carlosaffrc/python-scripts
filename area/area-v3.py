# Área de figuras geométricas
# Obtendo o raio através do prompt
# Definindo uma funcão


from math import pi


def circulo(raio):
    print("Área do círculo: ", pi * float(raio) ** 2)


if __name__ == "__main__":
    raio = input("Raio do círculo: ")
    circulo(raio)
