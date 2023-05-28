console_input = float(input("Digite um número:"))

if console_input < 1 or console_input > 2:
    print('Grau Inválido')
elif console_input == 1:
    print('A equação é do primeiro grau')
    a = float(input('Digite o valor de a:'))
    if a == 0:
        print('Valor de a inválido.')
    else:
        b = float(input('Digite o valor de b:'))
        x = -b / a
        print(f"O valor da raiz é {x:.2f}")
else:
    print('A equação é do segundo grau')
    a = float(input('Digite o valor de a:'))
    if a == 0:
        print('Valor de a inválido')
    else:
        b = float(input('Digite o valor de b:'))
        c = float(input('Digite o valor de c:'))
        discriminante = b ** 2 - 4 * a * c
        if discriminante < 0:
            print('A equação não possui raízes reais')
        elif discriminante == 0:
            raiz = -b / (2 * a)
            print(f'A equação possui uma raiz real: {raiz:.2f}')
        else:
            raiz1 = (-b - discriminante ** 0.5) / (2 * a)
            raiz2 = (-b + discriminante ** 0.5) / (2 * a)
            print(f'A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}')

            
                    

            

