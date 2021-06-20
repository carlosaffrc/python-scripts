#!/usr/bin/python3.9
# Leitura/Escrita de um arquivo CSV/TXT e impresão na tela
# Via streaming de dados usando a estrutura with
with open("pessoas.csv") as arquivo:
    with open("pessoas.txt", "w") as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(",")
            print("Nome: {} Idade: {}".format(*pessoa), file=saida)

if arquivo.closed:
    print("O arquivo foi fechado")

if saida.closed:
    print("O arquivo de saída foi fechado")
