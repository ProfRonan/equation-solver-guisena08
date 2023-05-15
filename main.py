numero = float(input("Digite um número:"))
if numero <1 or numero >2:
    print('Grau Invalido')
elif numero ==1:
    print('Equação do primeiro grau')  
    p1 = float(input('Digite o valor de a:'))
    if p1 ==0:
        print('Valor inválido.')
    else:
        p2 = float(input('Digite o valor de b:'))
        x = -p2 / -p1 
        print(f"o valor da raiz é {x:.2f}")   
else:
    print('Equação do segundo grau.')
    q1 = float(input('digite o valor de a:'))
    if q1 ==0:
        print('valor invalido!')
    else:
        q2 = float(input('digite o valor de b:'))
        q3 = float(input('digite o valor de c:'))
        x = q2 ** 2 - 4*q1*q3   
        if x < 0:
            print('A equação não possui raízes reais')
        elif x==0:
            y = -q2 /  (2 *q1)
            print(f'A equação possui uma raiz real{y:.2f}')
        else:
            if x >0:
             t = (-q2 - x **0.5)/(2*q1)
             a = (-q2 + x **0.5)/(2*q1) 
            print(f'`A equação possui duas raízes reais{t:.2f} e {a:.2f} ')  
                    

            

