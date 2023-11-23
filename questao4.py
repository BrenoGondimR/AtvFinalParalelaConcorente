import requests

# url
base_url = "https://belmondojr.dev/proc_paralelo.php"

# so um exemplo de matrizes
matrixA = [[1, 2], [3, 4]]
matrixB = [[5, 6], [7, 8]]

# definindo os parmaetros aqui
params = {
    "matrixA": str(matrixA),
    "matrixB": str(matrixB)
}

# solicitacao
response = requests.get(base_url, params=params)

# certo ou errado? verificacoes...
if response.status_code == 200:
    print("Resposta recebida com sucesso:")
    print(response.text)
else:
    print(f"Erro na solicitação: {response.status_code}")

