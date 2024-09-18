
def fatorial(n):
    if n < 0:
        return "Não existe fatorial de números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}.")