import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
matriz = ""
vez = 1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4, TCP
server_socket.bind((HOST, PORT))  # Liga o servidor ao IP e porta especificados
server_socket.listen(2) # Espera por conexões, aceita no máximo 2


print ("Esperando conexão do cliente 1")
client1_socket, client1_address = server_socket.accept() # Aceita a conexão do cliente, função bloqueante, espera até que um cliente se conecte
print("Cliente 1 conectado:", client1_address)
client1_socket.sendall('1'.encode()) # Envia o número do jogador para o cliente 1


print("Esperando broadcast")
BROADCAST_IP = "255.255.255.255"  
BROADCAST_PORT = 1234

server_socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPV4, UDP (User Datagram Protocol)
server_socketUDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Configura o socket para enviar broadcast
server_socketUDP.bind(("", BROADCAST_PORT)) # Liga o servidor a porta especifica e IP o SO escolhe

data, client_address = server_socketUDP.recvfrom(1024) # Espera receber uma mensagem de broadcast, função bloqueante, espera até que uma mensagem seja recebida
message = data.decode() # Decodifica a mensagem recebida

if message == "broadcast": # Se a mensagem for broadcast, envia o IP do servidor para o cliente
    server_ip = socket.gethostbyname(socket.gethostname()) 
    server_socketUDP.sendto(server_ip.encode(), client_address)

server_socketUDP.close() # Fecha o socket UDP


print ("Esperando conexão do cliente 2")
client2_socket, client2_address = server_socket.accept()
print("Cliente 2 conectado:", client2_address)
client2_socket.sendall('2'.encode())

while True:
    data1 = client1_socket.recv(1024).decode()
    data2 = client2_socket.recv(1024).decode()

    if (data1 != matriz) and (vez == 1):
        matriz = data1.encode()

    if (data2 != matriz) and (vez == 2):
        matriz = data2.encode()

    matrizReal = eval(matriz.decode())
    vez = matrizReal[3][2][2]

    client1_socket.sendall(matriz)
    client2_socket.sendall(matriz)

client1_socket.close()
client2_socket.close()
server_socket.close()