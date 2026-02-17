'''
Ana está desenvolvendo um programa que precisa processar uma lista 
de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela 
precisa escrever um programa que percorra a lista de nomes e exiba 
cada cliente.
'''

from rich import print 

clients = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for client in clients:
    print(f'[bold green]{client}[/bold green]')