import requests
import json

def get_data(url):
    """Faz uma requisição GET para a API"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para códigos de erro HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

def post_data(url, data):
    """Faz uma requisição POST para a API"""
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo usando a API pública JSONPlaceholder
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Exemplo de GET
    posts = get_data(f"{base_url}/posts/1")
    if posts:
        print("Dados recebidos via GET:")
        print(json.dumps(posts, indent=2))
    
    # Exemplo de POST
    novo_post = {
        "title": "Novo Post",
        "body": "Conteúdo do novo post",
        "userId": 1
    }
    
    resultado = post_data(f"{base_url}/posts", novo_post)
    if resultado:
        print("\nDados enviados via POST:")
        print(json.dumps(resultado, indent=2)) 
        import requests
import json

def get_data(url):
    """Faz uma requisição GET para a API"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para códigos de erro HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

def post_data(url, data):
    """Faz uma requisição POST para a API"""
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo usando a API pública JSONPlaceholder
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Exemplo de GET
    posts = get_data(f"{base_url}/posts/1")
    if posts:
        print("Dados recebidos via GET:")
        print(json.dumps(posts, indent=2))
    
    # Exemplo de POST
    novo_post = {
        "title": "Novo Post",
        "body": "Conteúdo do novo post",
        "userId": 1
    }
    
    resultado = post_data(f"{base_url}/posts", novo_post)
    if resultado:
        print("\nDados enviados via POST:")
        print(json.dumps(resultado, indent=2))