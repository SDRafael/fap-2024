# testando lambdas para calcular potencias e testando se um numero é par ou impar
def atividade_com_lambdas():
    
    dobro = lambda x: x * 2
    triplo = lambda x: x * 3
    eh_par = lambda x: "Par" if x % 2 == 0 else "Ímpar"
    
    
    numero = int(input("Digite um número inteiro: "))
    
    
    print(f"\nNúmero digitado: {numero}")
    print(f"O dobro de {numero} é: {dobro(numero)}")
    print(f"O triplo de {numero} é: {triplo(numero)}")
    print(f"{numero} é: {eh_par(numero)}")

# Executa a função
atividade_com_lambdas()
