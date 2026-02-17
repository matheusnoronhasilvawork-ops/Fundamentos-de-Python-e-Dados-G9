
from rich import print

projects = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for project in projects:
    if project is None:
        print(f"[bold red]missing project[bold red]")
    else:
        print(project)

dados = {"nome": "Tarciana", "idade": 20}
print(dados)

from rich.json import JSON
from rich.console import Console

console = Console()
console.print(JSON('{"nome": "Tarciana", "idade": 20}'))

from rich.progress import track
import time

for step in track(range(10), description="Processando..."):
    print(f"Step {step + 1}/10")
    time.sleep(0.5)