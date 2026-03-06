# YASMIN
print("----- Sistema de Log Natural -----")
print("")

x = float(input("Digite um número maior que 0: "))

while x <= 0:
    print("Número inválido!")
    x = float(input("Digite um número maior que 0: "))

arredondamento = int(input("Digite o máximo de repeticões que deseja (ideal, 20): "))

soma = 0
n = 0

while n <= arredondamento:
    termo = (1 / (2*n + 1)) * (((x - 1) / (x + 1)) ** (2*n + 1))
    soma = soma + termo
    n = n + 1

resultado = 2 * soma

print("")
print(f"ln({x}) ≈ {resultado}")


print("Ola a todos")

# MARIA
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

#pedro
#exponencial 

def exponencial (x, termos=50):
    termo_atual = 1.0
    resultado = 1
    
    for i in range (1, termos):
        termo_atual = termo_atual * x / i
        resultado += termo_atual
        
    return resultado

x = float(input("digite seu numero: "))

print(exponencial(x))
