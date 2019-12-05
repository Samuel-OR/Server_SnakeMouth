
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
                if self.MYSQL.cadastrar_no_banco(recebido[4],recebido[1],recebido[2],recebido[3]):
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())
            
            if recebido[0] == "login":
                status,usuario,times =  self.MYSQL.verifica_login(recebido[1],recebido[2])
                if status:
                    resposta = "okLogin,"
                    resposta += str(usuario[0][0])+','
                    resposta += str(usuario[0][1])+','
                    resposta += str(usuario[0][2])+','
                    resposta += str(usuario[0][3])+','
                    resposta += str(usuario[0][4])+','
                    resposta += str(times)+','
                    resposta += str(usuario[0][5])
                    self.csocket.send(resposta.encode())

                else:
                	self.csocket.send("error".encode())

            if recebido[0] == "loginTime":
                print("Login Time")
                status,usuario =  self.MYSQL.verifica_loginTime(recebido[1],recebido[2])
                if status:
                    resposta = "okLogin,"
                    resposta += str(usuario[0][0])+','
                    resposta += str(usuario[0][1])+','
                    resposta += str(usuario[0][2])+','
                    resposta += str(usuario[0][3])+','
                    resposta += str(usuario[0][4])+','
                    resposta += str(usuario[0][5])
                    self.csocket.send(resposta.encode())
                else:
                    self.csocket.send("error".encode())

            if recebido[0] == "cadastroTime":
                string_cadastro_time=""
                string_cadastro_time+=recebido[2]+","+recebido[3]+","+recebido[4]+","+recebido[5]
                if self.MYSQL.cadastrarTime(recebido[1],string_cadastro_time,recebido[6], recebido[7]): 
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())

            if recebido[0] == "cadastrarExer":
                print("Receiver:", recebido)
                if self.MYSQL.cadastrarExer(recebido[1],recebido[2],recebido[3],recebido[4],recebido[5],recebido[6]):
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())

            if recebido[0] == "buscaTime":
                status,time = self.MYSQL.busca_time_editar(recebido[1])
                if status:
                    print("Busca Time: ",time)
                    resposta = "okBuscaTime,"
                    resposta+=str(time[0][0])+','
                    resposta+=str(time[0][1])+','
                    resposta+=str(time[0][2])+','
                    resposta+=str(time[0][3])+','
                    resposta+=str(time[0][4])+','
                    resposta+=str(time[0][5])+','
                    self.csocket.send(resposta.encode())

            if recebido[0] == "editarTime":
                print("Receiver: ",recebido)
                string_editar_time=""
                string_editar_time+=recebido[2]+","+recebido[3]+","+recebido[4]+","+recebido[5]

                if self.MYSQL.editarTime(recebido[1],string_editar_time,recebido[6]): 
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())

            if recebido[0] == "editarProfessor":
                print("Receiver: ",recebido)
                if self.MYSQL.editarProfessor(recebido[1],recebido[2],recebido[3],recebido[4], recebido[5]):
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())

            if recebido[0] == "listarTimes":
                status,time = self.MYSQL.listarTimes(recebido[1])

                if status:
                    resposta = str('okListarTimes')
                    for x in time:
                        resposta+=';'
                        resposta += str(x[0])+','
                        resposta += str(x[1])+','
                        resposta += str(x[2])+','
                        resposta += str(x[3])+','
                        resposta += str(x[4])+','
                        resposta += str(x[5])
                    
                    self.csocket.send(resposta.encode()) 

            if recebido[0] == "pegarExercicios":
                status,time = self.MYSQL.pegarExercicios(recebido[1])

                if status:
                    resposta = str('okPegarExercicios')
                    for x in time:
                        resposta+=';'
                        resposta += str(x[0])+','
                        resposta += str(x[1])+','
                        resposta += str(x[2])+','
                        resposta += str(x[3])+','
                        resposta += str(x[4])+','
                        resposta += str(x[5])
                    
                    self.csocket.send(resposta.encode())

            if recebido[0] == "atualizarHistorico":
                status,time = self.MYSQL.pegarHistorico(recebido[1])
                if status:
                    resposta = str('okatualizarHistorico')
                    for x in time:
                        resposta+=';'
                        resposta += str(x[0])+','
                        resposta += str(x[1])+','
                        resposta += str(x[2])+','
                        resposta += str(x[3])+','
                        resposta += str(x[4])
                    
                    self.csocket.send(resposta.encode())
            
            if recebido[0] == "cadastrarHist":
                print("Receiver:", recebido)
                if self.MYSQL.cadastrarHist(recebido[1],recebido[2],recebido[3],recebido[4]):
                    self.csocket.send("ok".encode())
                else:
                    self.csocket.send("error".encode())

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
