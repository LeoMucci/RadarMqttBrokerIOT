
# 🚦 **Radar de Velocidade com MQTT** 📡

---
### 👤 Integrantes:
- Juliana Alves
- Leonardo Mucci
- Marcos Vinicius
- Rodrigo Veloso

---
## 🌟 **Resumo do Projeto**

Este projeto simula um sistema de **radar de velocidade** que utiliza o protocolo MQTT para comunicação entre dois componentes principais:  
- O **Radar (Publicador)** envia informações de velocidade detectadas de veículos para um **servidor MQTT (broker)**.  
- O **Central de Controle (Assinante)** recebe essas velocidades, verifica se elas ultrapassam o limite permitido, e registra uma multa quando necessário.  

Esse sistema foi criado para demonstrar como tecnologias simples podem ser usadas para resolver problemas reais, como o monitoramento de velocidade em rodovias. 🚗💨

---

## 🎯 **Por que Criamos Este Sistema?**

Com o aumento de veículos nas estradas e o desafio de manter a segurança no trânsito, radares de velocidade são ferramentas essenciais para:
1. **Monitorar velocidades em tempo real.**
2. **Garantir a segurança no tráfego, identificando excessos.**
3. **Automatizar o processo de detecção e notificação de infrações.**

Este projeto exemplifica como soluções baseadas em MQTT podem ser implementadas para atender a essas necessidades, tornando o sistema mais ágil, escalável e eficiente. 🚀

---

## 📋 **Estrutura do Sistema**

1. **📡 Radar (Publisher):**  
   - Detecta a velocidade dos veículos em rodovias.
   - Publica os dados em um broker MQTT, que age como intermediário.

2. **🖥️ Central de Controle (Receiver):**  
   - Escuta os dados enviados pelo radar.
   - Avalia as velocidades:
     - **Dentro do limite**: Veículo está em conformidade.
     - **Acima de 100 km/h**: 🚨 Gera uma multa.

3. **⚙️ Broker MQTT:**  
   - Gerencia as mensagens entre o radar e a central.

---

## 📁 **Cenário Realista de Aplicação**

Imagine uma **rodovia monitorada por radares** instalados em pontos estratégicos:

1. O radar detecta veículos e suas velocidades ao passarem.  
   - **Exemplo:** Um carro passou a **105 km/h**.  

2. A velocidade é enviada para um broker central (no servidor).  
   - O broker atua como um "mensageiro" entre o radar e a central.

3. A central recebe a velocidade e verifica:  
   - **Se for acima de 100 km/h:** 🚨 MULTA!  
   - **Se for igual ou menor a 100 km/h:** 👍 Dentro do limite.

4. A multa gerada pode ser armazenada no banco de dados e enviada ao condutor identificado. 📬

---

## 🛠️ **Tecnologias Utilizadas**

- **Python**: Linguagem principal para automação do radar. 🐍  
- **Paho MQTT**: Biblioteca para comunicação MQTT. 📡  
- **dotenv**: Para gerenciar variáveis sensíveis como IP e porta do broker. 🔐  
- **Mosquitto**: Broker MQTT usado no servidor.  

---

## 🚦 **Funcionamento do Código**

### **1. Radar (Publicador)**  
- Detecta velocidades aleatórias entre 30 km/h e 120 km/h.  
- Publica os dados no broker no tópico configurado (`radar/velocidade`).

#### 🔑 **Trecho Principal:**
```python
velocidade = random.randint(30, 120)
cliente.publish(topico, velocidade)
print(f"Velocidade enviada: {velocidade} km/h")
```

---

### **2. Central de Controle (Assinante)**  
- Recebe as velocidades do broker.  
- Analisa se estão acima de **100 km/h** para sinalizar multas.

#### 🔑 **Trecho Principal:**
```python
if velocidade > 100:
    print(f"Velocidade: {velocidade} km/h - MULTA! Acima do limite.")
else:
    print(f"Velocidade: {velocidade} km/h - Dentro do limite permitido.")
```

---

## 🌍 **Exemplo de Saída**

### **Radar (Publisher):**
```
Velocidade enviada: 90 km/h
Velocidade enviada: 105 km/h
Velocidade enviada: 78 km/h
```

### **Central (Receiver):**
```
Velocidade: 90 km/h - Dentro do limite permitido.
Velocidade: 105 km/h - MULTA! Acima do limite.
Velocidade: 78 km/h - Dentro do limite permitido.
```

---

## 🚀 **Como Configurar e Executar**

### **1. Instale as dependências**
```bash
pip install paho-mqtt python-dotenv
```

### **2. Configure o `.env`**
Adicione as configurações do broker:
```dotenv
BROKER_IP=SEU_IP_DO_BROKER
BROKER_PORT=1883
TOPICO=radar/velocidade
```

### **3. Execute o Publicador**
```bash
python publisher.py
```

### **4. Execute o Assinante**
```bash
python receiver.py
```

---


