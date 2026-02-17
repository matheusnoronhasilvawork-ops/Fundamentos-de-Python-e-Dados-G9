'''
Ana está desenvolvendo seu portfólio para exibir os projetos de Python 
que concluiu. Ela organizou uma lista com o nome de cada projeto, mas 
percebeu que alguns itens podem estar ausentes, aparecendo como 
None:

Crie um programa que ajude Ana a percorrer a lista de projetos e exiba 
os nomes dos projetos válidos. Se encontrar um item None, o programa 
deve exibir a mensagem: "Projeto ausente".
'''

from rich import print

projects = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for project in projects:
    if project is None:
        print(f"[bold red]missing project[bold red]")
    else:
        print(project)

