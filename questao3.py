import requests
import random
import time

def coletar_dados_sensor():
    # Simulando dados de sensores
    temperatura = random.uniform(20.0, 30.0)  # Temperatura em graus Celsius
    umidade = random.uniform(30.0, 70.0)      # Umidade em porcentagem

    return temperatura, umidade

def enviar_dados_para_analise(temperatura, umidade):
    # URL para onde os dados dos sensores serão enviados
    url_sensores = "https://belmondojr.dev/sensores.php"

    # Parâmetros a serem enviados
    parametros = {
        'temperatura': temperatura,
        'umidade': umidade
    }

    # Enviando os dados para o servidor
    try:
        resposta = requests.get(url_sensores, params=parametros)
        print("Dados enviados. Código de Status:", resposta.status_code)
        print("Resposta do Servidor:", resposta.text)
    except Exception as e:
        print("Erro ao enviar dados para análise:", str(e))

# Coletando e enviando dados periodicamente
while True:
    temperatura, umidade = coletar_dados_sensor()
    enviar_dados_para_analise(temperatura, umidade)
    time.sleep(10)
