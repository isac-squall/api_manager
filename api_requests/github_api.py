import requests

def get_github_user(username):
    """Obtém informações de um usuário do GitHub"""
    url = f"https://api.github.com/users/{username}"
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar usuário: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    usuario = get_github_user("octocat")
    if usuario:
        print(f"Nome: {usuario.get('name')}")
        print(f"Seguidores: {usuario.get('followers')}")
        print(f"Repositórios públicos: {usuario.get('public_repos')}")

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json()
