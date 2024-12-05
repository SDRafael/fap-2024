#Modificando o código para tratar exceptions
def calcular_imc(altura,peso):
    try:
        
        imc = peso / (altura ** 2)

        
        categorias = [
            ("Abaixo do peso", 0, 18.5),
            ("Peso normal", 18.5, 24.9),
            ("Sobrepeso", 25, 29.9),
            ("Obesidade grau 1", 30, 34.9),
            ("Obesidade grau 2", 35, 39.9),
            ("Obesidade grau 3", 40, float('inf'))
        ]

        
        print(f"\nSeu IMC é: {imc:.2f}\n")

        
        print("Categorias de IMC:")
        for categoria, limite_inferior, limite_superior in categorias:
            print(f"- {categoria}: {limite_inferior} a {limite_superior}")
            if limite_inferior <= imc <= limite_superior:
                print(f"  * Você se encontra nesta categoria: {categoria} *")

    except ValueError:
        print("Por favor, insira valores válidos para altura e peso.")


altura = float(input("Digite sua altura em metros (exemplo: 1.72): "))
peso = float(input("Digite seu peso em kg (exemplo: 72): "))
calcular_imc(altura,peso)
