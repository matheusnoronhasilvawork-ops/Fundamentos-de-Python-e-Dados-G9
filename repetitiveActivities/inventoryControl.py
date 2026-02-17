'''
Você está desenvolvendo um sistema de controle de estoque para o 
Buscante. Um dos requisitos é verificar a quantidade de exemplares de 
um livro em estoque e continuar vendendo até que o estoque se esgote. 
Sempre que uma venda é realizada, o sistema deve informar o usuário e 
atualizar a quantidade disponível.

Crie um programa que simule as vendas de um livro com o estoque 
inicial de 5 exemplares. O programa deve exibir a mensagem "Venda 
realizada! Estoque restante: <quantidade>" a cada venda e, ao final, 
exibir a mensagem "Estoque esgotado".
'''

from rich import print

book_inventory = 5

while book_inventory  > 0:
    book_inventory -= 1
    print(
        f'book sold! \n'
        f'[bold purple]books left: {book_inventory}[/bold purple]'
        )

print('[bold red]Out of stock![/bold red]')