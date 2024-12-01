import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()
broker = os.getenv("BROKER_IP")
porta = int(os.getenv("BROKER_PORT"))
topico = os.getenv("TOPICO")

# Limite de velocidade para multa
limite_multa = 100 

# Função chamada ao receber mensagens
def on_message(client, userdata, msg):
    velocidade = int(msg.payload.decode())
    if velocidade > limite_multa:
        print(f"Velocidade: {velocidade} km/h - MULTA! Velocidade muito acima do limite permitido de {limite_multa} km/h.")
    else:
        print(f"Velocidade: {velocidade} km/h - Dentro do limite permitido.")

# Configuração do cliente assinante
def verificar_velocidade():
    cliente = mqtt.Client()
    try:
        cliente.connect(broker, porta, 60)
        cliente.on_message = on_message
        cliente.subscribe(topico)
        print(f"Inscrito no tópico: {topico}")
        cliente.loop_forever()  
    except Exception as e:
        print(f"Erro ao conectar/assinar: {e}")

if __name__ == "__main__":
    verificar_velocidade()
