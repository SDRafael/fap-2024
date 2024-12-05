#melhorando um conversor de temperatura utilizando lambdas
def converterTtemperatura():
    # Funções lambda para conversões
    celsius_para_fahrenheit = lambda c: (c * 9/5) + 32
    fahrenheit_para_celsius = lambda f: (f - 32) * 5/9
    celsius_para_kelvin = lambda c: c + 273.15
    kelvin_para_celsius = lambda k: k - 273.15
    
    print("\nEscolha a conversão:")
    print("1. Celsius para Fahrenheit e Kelvin")
    print("2. Fahrenheit para Celsius e Kelvin")
    print("3. Kelvin para Celsius e Fahrenheit")
    
    
    opcao = int(input("\nDigite a opção desejada (1, 2 ou 3): "))
    
    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        kelvin = celsius_para_kelvin(celsius)
        print(f"\n{celsius}°C é equivalente a:")
        print(f"{fahrenheit:.2f}°F")
        print(f"{kelvin:.2f}K")
    
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        kelvin = celsius_para_kelvin(celsius)
        print(f"\n{fahrenheit}°F é equivalente a:")
        print(f"{celsius:.2f}°C")
        print(f"{kelvin:.2f}K")
    
    elif opcao == 3:
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        celsius = kelvin_para_celsius(kelvin)
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"\n{kelvin}K é equivalente a:")
        print(f"{celsius:.2f}°C")
        print(f"{fahrenheit:.2f}°F")
    
    else:
        print("Opção inválida! Tente novamente.")

converterTtemperatura()
