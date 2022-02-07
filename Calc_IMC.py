nome = input('Por favor digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

print( 'Olá',nome,', seu indice de massa corporal é {:.2f} \n'.format(imc))

if imc < 16:
    print('Subpeso Severo\n ')

if imc >= 16 and imc < 19.9:
    print('Subpeso\n ')    

if imc >= 20 and imc < 24.9:
    print('Normal\n') 

if imc >= 25 and imc < 29.9:
    print('Sobrepeso\n') 

if imc >= 30 and imc < 39.9:
    print('Obeso\n ') 

if imc >= 40:
    print('Obeso Mórbido \n ')
