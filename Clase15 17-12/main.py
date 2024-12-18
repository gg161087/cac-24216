#pip install --user requests
import requests
from colorama import init, Fore
init() # Inicializa Colorama

URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

def get_data():
    res = requests.get(URL)
    if res.status_code == 200:
        result = res.json()
        repositorios = result['items']
        print(f'Total de Repositorios: {result['total_count']}')
        primer_repo = repositorios[0]
        imprimir_repo(primer_repo)

def imprimir():
    print(Fore.GREEN + "Este mensaje se muestra en verde.")
    print(Fore.RED + "Este mensaje se muestra en rojo.")

def imprimir_repo(repo):
    print(f'Name: {repo['name']}')
    print(f'Owner {repo['owner']['login']}')
    print(f'Stars: {repo['stargazers_count']}')
    print(f'Repository: {repo['html_url']}')
    print(f'Description: {repo['description']}')

if __name__ == "__main__":
    imprimir()
    get_data()
