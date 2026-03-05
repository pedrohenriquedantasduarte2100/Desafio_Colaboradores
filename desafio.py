print("Ola a todos")

# Número de Euler (e)

def fatorial(n): 
    resultado = 1 # vai sempre começar com 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado

def numero_e(termos): # vai se basear no número q a pessoa digitar
    soma = 0
    for n in range(termos):
        soma = soma + 1 / fatorial(n)
    return soma

print("**** Calculando o Número de Euler **** ")
print("")
termos = int(input("Digite o máximo de repetições que deseja (o idea seria 20 para ter uma melhor precisão): "))
print(f"O Resultado do Número de Euler é ≈ {numero_e(termos)}")