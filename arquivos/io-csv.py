#!/usr/bin/python3.9
# Leitura de um arquivo CSV
# Usando a API nativa do python
import csv

with open("pessoas.csv") as entrada:
    for pessoa in csv.reader(entrada):
        print("Nome: {} Idade: {}".format(*pessoa))
