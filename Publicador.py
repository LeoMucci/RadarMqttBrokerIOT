import paho.mqtt.client as mqtt
import random
import time
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()
broker = os.getenv("BROKER_IP")
porta = int(os.getenv("BROKER_PORT"))
topico = os.getenv("TOPICO")

# Função para publicar velocidades
def publicar_velocidade():
    cliente = mqtt.Client()
    try:
        cliente.connect(broker, porta, 60)
        print("Conectado ao broker!")
        
        while True:
            velocidade = random.randint(30, 120)
            cliente.publish(topico, velocidade)
            print(f"Velocidade enviada: {velocidade} km/h")
            time.sleep(3) 
    except Exception as e:
        print(f"Erro ao conectar/publicar: {e}")

if __name__ == "__main__":
    publicar_velocidade()
