#!/usr/bin/python3.9
# Leitura de um arquivo e impresão na tela
# Via streaming de dados
# Com remocão dos espacos entre linhas
# Usando try/finally p/ garantir o arquivo foi fechado
try:
    arquivo = open("pessoas.csv")

    for registro in arquivo:
        print("Nome: {} Idade: {}".format(*registro.strip().split(",")))
finally:
    print("finally")
    arquivo.close()

if arquivo.closed:
    print("O arquivo foi fechado")
