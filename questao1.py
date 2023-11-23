import requests

def enviar_dados_para_servidor():

    temperatura_mockada = 24.5  # Temperatura de exemplo

    url_servidor = "https://belmondojr.dev/comunicacao.php"

    # Parâmetros a serem enviados
    # Aqui, estamos enviando 'sensors' como uma lista
    parametros = [
        ('sensors[]', 'temperature'),
        ('temperature', temperatura_mockada)
    ]

    # Enviando os dados para o servidor
    try:
        resposta = requests.get(url_servidor, params=parametros)
        print("Código de Status:", resposta.status_code)
        print("Resposta do Servidor:", resposta.text)
    except Exception as e:
        print("Erro ao enviar dados para o servidor:", str(e))


enviar_dados_para_servidor()
