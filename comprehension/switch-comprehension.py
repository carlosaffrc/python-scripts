#!/usr/bin/python3.9


def get_tipo_dia(dia):
    dias = {
        (1, 7): "Fim de semana",
        tuple(range(2, 7)): "Dia de semana",
    }
    dia_escolhido = (tipo for num, tipo in dias.items() if dia in num)
    return next(dia_escolhido, "** dia inválido **")


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"{dia}: {get_tipo_dia(dia)}")
