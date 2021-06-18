#!/usr/bin/pythoh3.9
# 0, 1, 2, 3, 5, 8, 13, 21...


def fibonacci():
    limite = 10000
    penultimo = 0
    ultimo = 1
    print(f"{penultimo},{ultimo}", end=",")
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=",")
        penultimo = ultimo
        ultimo = proximo

        if ultimo > limite:
            break


if __name__ == "__main__":
    fibonacci()
