'''
João está desenvolvendo um sistema de cadastro para um site de leitura. 
Ele precisa garantir que os usuários insiram um nome de usuário e uma 
senha válidos. As regras são as seguintes:

- O nome de usuário deve ter pelo menos 5 caracteres.

- A senha deve ter pelo menos 8 caracteres.

João quer que o sistema continue solicitando as informações até que 
ambas as condições sejam atendidas. Quando o usuário insere dados 
válidos, o programa deve exibir a mensagem: "Cadastro realizado com 
sucesso!".

Crie um programa que implemente essa lógica usando um laço while.
'''


while True:
    username = str(input('Enter your userName: '))
    password = str(input('Enter your password: '))

    if len(username) < 5:
        print('userName must be at least 5 characters')
    elif len(password) < 8:
        print('password must be at least 8 characters')
    else:
        print('Login successful')
        break
