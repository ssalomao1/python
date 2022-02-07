LoginUser = 'Salomão'
Dtnascuser = '29/06/2000'

Login = input('Digite seu nome: ')
if Login != LoginUser:
    print('Acesso Negado')
    exit()
DTnasc = input('Digite sua Data de nascimento: ')
if Login == LoginUser and DTnasc == Dtnascuser:
    print('Bem-vindo',LoginUser)
else: 
    print('Acesso Negado')
