
import socket, threading
from mysqlbancodedados import MysqlBanco

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        self.MYSQL = MysqlBanco()
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)


    def run(self):
        print ("Conectado de: ", clientAddress)
        msg = ''
        data = ''
        while True:

            data = self.csocket.recv(1024)
            recebido = data.decode()
            recebido = recebido.split(',')
            print(recebido)
            if recebido[0] == "cadastro":
                if self.MYSQL.cadastrar_no_banco("2019",recebido[1],recebido[2],recebido[3]):
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())
            if recebido[0] == "login":
                self.MYSQL.verifica_login(recebido[1],recebido[2])

            if recebido[0] == "cadastroTime":
                string_cadastro_time=""
                string_cadastro_time+=recebido[2]+","+recebido[3]+","+recebido[4]+","+recebido[5]
                if self.MYSQL.cadastrarTime(recebido[1],string_cadastro_time):
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())

        """
        msg = data.decode()
        print("REceiver: ", msg)
        
        lista = msg.split(',')

        user= lista[0]
        password = lista[1]
        name = lista[1]
        """

        self.csocket.send("cad".encode())
        

        print ("Client at ", clientAddress , " disconnected...")
if __name__ == '__main__':
    LOCALHOST = ''
    PORT = 7000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
