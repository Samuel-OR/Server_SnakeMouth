import socket

class Servidor(object):
	
	def __init__(self):
		self.host = ""
		self.port = 7008
		self.address = (self.host, self.port)
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criar socket
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.connection = ""

	def start_server(self):
		self.server_socket.bind(self.address)
		self.server_socket.listen(10)

		print("Loading...")
		self.connection, cliente = self.server_socket.accept()
		while True:
			print("Conectado")
			receiver = self.connection.recv(1024).decode()
			print(receiver)

			self.connection.send("Dados recebidos.".encode())
 
	def break_server(self):
		self.server_socket.close()

server = Servidor()
server.start_server()