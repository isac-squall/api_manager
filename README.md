exemplo que mostra como fazer diferentes tipos de requisições HTTP:
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
        ###########################################################################################################################################################################################################
        Este código demonstra:
Como fazer requisições GET para obter dados
Como fazer requisições POST para enviar dados
Tratamento de erros básico
Uso de headers
Manipulação de JSON
Para usar este código, você precisa primeiro instalar a biblioteca requests:
##############################################################################################################################################################################################################
pip install requests
#####################################################################################################################################################################################################
Alguns pontos importantes sobre o código:
A função get_data() faz requisições GET simples e retorna os dados em formato JSON
A função post_data() envia dados para a API usando o método POST
Ambas as funções incluem tratamento de erros básico
O exemplo usa a API JSONPlaceholder, que é uma API pública de teste
Para adaptar este código para uma API específica, você precisaria:
Alterar a URL base
Ajustar os headers conforme necessário (por exemplo, adicionar tokens de autenticação)
Modificar a estrutura dos dados enviados/recebidos de acordo com a API
Aqui está um exemplo mais específico usando a API do GitHub:
#################################################################################################################################################################################
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
usuario = get_github_user("octocat")
if usuario:
    print(f"Nome: {usuario.get('name')}")
    print(f"Seguidores: {usuario.get('followers')}")
    print(f"Repositórios públicos: {usuario.get('public_repos')}")
    ##############################################################################################################################################################
    Dicas importantes ao trabalhar com APIs:
Sempre verifique a documentação da API
Implemente rate limiting quando necessário
Armazene tokens e credenciais de forma segura
Use try/except para tratar erros
Verifique os códigos de status HTTP
Considere usar async/await para requisições assíncronas em aplicações maiores
