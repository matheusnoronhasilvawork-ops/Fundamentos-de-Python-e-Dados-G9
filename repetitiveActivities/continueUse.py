'''
Ana está implementando um sistema de filtragem de livros no Buscante. 
A funcionalidade deve percorrer uma lista de livros e exibir o nome de 
cada livro disponível em estoque. No entanto, se o livro estiver esgotado, 
ele deve ser ignorado durante a iteração.

Crie um programa que ajude Ana a exibir somente os livros que 
possuem estoque disponível, no formato: "Livro disponível: ".

'''

from rich import print

books = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for book in books:
    if book["estoque"] > 0:
        print(f'[bold green]book available: {book['nome']}[/bold green]')