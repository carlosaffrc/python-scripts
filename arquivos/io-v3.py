#!/usr/bin/python3.9
# Leitura de um arquivo e impresão na tela
# Via streaming de dados
# Com remocão dos espacos entre linhas
arquivo = open("pessoas.csv")

for registro in arquivo:
    print("Nome: {} Idade: {}".format(*registro.strip().split(",")))

arquivo.close()
