import socket 

ip = '127.0.0.1'
port = 60000
buffer = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_bind = (ip, port)

server_socket.bind(server_bind)

server_socket.listen()

server_socket.accept()


print(server_socket)

while True: 
    
    print("aguardando conexão... :")
    client_connection, client_addr = server_socket.accept()

    print("Conexão estabelecida = {}".format(client_connection))

    while True:
        data_client = client_connection.recv(buffer)

        if not data_client:
            break

        print("msg do cliente = {}".format(data_client))

        message = b"msg do servidor para o cliente"

        client_connection.send(message)