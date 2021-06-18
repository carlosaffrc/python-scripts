#!/usr/bin/python3.9
def fibonacci(quant, seq=(0, 1)):
    # Condicão de parada
    return seq if len(seq) == quant else fibonacci(quant, seq + (sum(seq[-2:]),))


if __name__ == "__main__":
    # Sequência com os 30 primeiros termos
    for fib in fibonacci(30):
        print(fib)
