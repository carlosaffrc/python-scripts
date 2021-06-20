#!/usr/bin/python3.9
# Leitura de um arquivo e impresão na tela
# Via streaming de dados usando a estrutura with
with open("pessoas.csv") as arquivo:
    for registro in arquivo:
        print("Nome: {} Idade: {}".format(*registro.strip().split(",")))

if arquivo.closed:
    print("O arquivo foi fechado")
