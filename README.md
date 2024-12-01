
# 🚦 Radar de Velocidade com MQTT 📡

Este é um projeto que simula um sistema de **radar de velocidade** para monitoramento de rodovias utilizando o protocolo MQTT. Ele é composto por dois principais componentes:

1. **Radar (Publisher):** Envia informações de velocidade detectadas para o broker MQTT.
2. **Central de Controle (Receiver):** Recebe as velocidades e verifica se estão acima do limite permitido (100 km/h).

---
### 👤 Integrantes:
- Juliana Alves
- Leonardo Mucci
- Marcos Vinicius
- Rodrigo Veloso

---
## 🎯 Objetivo

Demonstrar como tecnologias distribuídas podem ser usadas para criar sistemas práticos, escaláveis e eficientes, com foco na segurança rodoviária.

---

## 📁 Estrutura do Projeto

- **`publisher.py`**: Código para o radar que publica velocidades.
- **`receiver.py`**: Código para a central que analisa as velocidades recebidas.
- **`.env`**: Arquivo para armazenar configurações sensíveis como o IP do broker, porta e tópico MQTT.

---

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍
- **Paho MQTT** 📡
- **dotenv** 🔐
- **Mosquitto Broker**

---

## 🚦 Funcionamento

### **Publisher (Radar):**
- Detecta velocidades aleatórias entre 30 km/h e 120 km/h.
- Publica as velocidades no tópico MQTT configurado no `.env`.

### **Receiver (Central):**
- Recebe as velocidades do broker MQTT.
- Avalia as velocidades:
  - **Até 100 km/h:** Dentro do limite.
  - **Acima de 100 km/h:** 🚨 MULTA!

---

## 🌍 Exemplo de Saída

### **Publisher:**
```
Velocidade enviada: 95 km/h
Velocidade enviada: 110 km/h
Velocidade enviada: 80 km/h
```

### **Receiver:**
```
Velocidade: 95 km/h - Dentro do limite permitido.
Velocidade: 110 km/h - MULTA! Acima do limite.
Velocidade: 80 km/h - Dentro do limite permitido.
```

---

## 🚀 Como Configurar e Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/radar-mqtt.git
   cd radar-mqtt
   ```

2. **Instale as dependências:**
   ```bash
   pip install paho-mqtt python-dotenv
   ```

3. **Configure o `.env`:**
   Crie o arquivo `.env` e adicione:
   ```dotenv
   BROKER_IP=SEU_IP_DO_BROKER
   BROKER_PORT=1883
   TOPICO=radar/velocidade
   ```

4. **Execute o Publicador:**
   ```bash
   python publisher.py
   ```

5. **Execute o Assinante:**
   ```bash
   python receiver.py
   ```

---

## 📜 Licença

Este projeto é apenas para fins educacionais e está disponível sob a licença MIT.

---

Com este sistema, você pode explorar como tecnologias distribuídas e o protocolo MQTT podem ser aplicados a problemas do mundo real! 🚗💨
