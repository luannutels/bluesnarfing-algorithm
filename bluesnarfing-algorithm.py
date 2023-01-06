import bluetooth

# Endereço MAC do alvo
alvo = "00:11:22:33:44:55"

# Tenta se conectar ao alvo
try:
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((alvo, 1))
except bluetooth.btcommon.BluetoothError as e:
    print("Erro ao se conectar:", e)
    exit()

# Envia um comando para o alvo solicitando informações de contatos
sock.send("CONTATOS")

# Recebe a resposta do alvo
resposta = sock.recv(1024)

# Fecha a conexão
sock.close()

# Exibe a resposta
print(resposta.decode())
