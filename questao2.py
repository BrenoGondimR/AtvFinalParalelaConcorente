import requests

def realizar_compra(produtos, precos):
    # URL do servidor para o qual os dados da compra serão enviados
    url_compra = "https://belmondojr.dev/compra.php"

    # Preparando os parâmetros para a requisição
    parametros = []
    for produto, preco in zip(produtos, precos):
        parametros.append(('products[]', produto))
        parametros.append(('values[]', preco))

    # Enviando os dados de compra para o servidor
    try:
        resposta = requests.get(url_compra, params=parametros)
        print("Código de Status:", resposta.status_code)
        print("Resposta do Servidor:", resposta.text)
    except Exception as e:
        print("Erro ao realizar a compra:", str(e))

# Exemplo de uso
produtos = ['Item1', 'Item2']  # Lista de produtos
precos = [10.50, 20.75]  # Lista de preços correspondentes

realizar_compra(produtos, precos)
