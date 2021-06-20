#!/usr/bin/python3.9
# Leitura de um arquivo e impresão na tela
# Através da funcão read()
arquivo = open("pessoas.csv")
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print("Nome: {}, Idade: {}".format(*registro.split(",")))
