'''
André está testando um novo recurso no backend do Buscante que 
processa dados em um loop. Durante os testes, ele percebeu que 
o sistema parou de responder, e suspeita que o problema está em um loop 
infinito.

Resolvido
'''

counter = 0

while counter < 10:
    print("Processing data...")
    counter += 1