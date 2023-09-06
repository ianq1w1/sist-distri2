import socket

ip_server = "127.0.0.1"
port_server = 60000
buffer = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

end_point_server = (ip_server, port_server)

client_socket.connect(end_point_server)

message = b"e o pix? nada ainda?"

client_socket.send(message)
data_server = client_socket.recv(buffer)

print("msg do server = {}".format(data_server))

client_socket.close()