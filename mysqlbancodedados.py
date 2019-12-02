import pymysql

class MysqlBanco():
	count = 0
	def __init__(self):

		self.host = "localhost"
		self.banco = "pooii"
		self.user = "root"
		self.password = "Samuel12345"
		self.conexao = pymysql.connect(host=self.host,db=self.banco,user=self.user,passwd=self.password)

	def iniciar_conexao(self):
		try:
			self.conexao = pymysql.connect(host=self.host,db=self.banco,user=self.user,passwd=self.password)
			print("Conectado ao banco de dados")
		except:
			print("Falha ao conectar no banco de dados")
			
	def cadastrar_no_banco(self,siape,nome,email,senha):
		cursor = self.conexao.cursor()
		query = "INSERT INTO professor(siape,nome,email,senha) VALUES(%s,%s,%s,%s)"
		cadastrado = False

		try:
			cursor.execute(query,(siape,nome,email,senha))
			self.conexao.commit()
			print("OK, Salvo no banco de dados")
			cadastrado = True
		except:
			print("Erro ao salvar no banco de dados!!!!!")

		return cadastrado

	def cadastrarTime(self,nomeTime,membros,professor):

		cursor = self.conexao.cursor()
		query = "INSERT INTO times_coders(nome_time,componentes_grupo,usuario) VALUES(%s,%s,%s)"
		cadastrado = False

		try:
			cursor.execute(query,(nomeTime,membros,professor))
			MysqlBanco.count+=1
			self.conexao.commit()
			print("OK, Salvo no banco de dados")
			cadastrado = True
		except:
			print("Erro ao salvar no banco de dados!!!!!")

		return cadastrado


	def verifica_login(self,usuario,senha):
		cursor = self.conexao.cursor()
		querySelect = "SELECT * FROM professor WHERE email=%s AND senha=%s"
		cursor.execute(querySelect,(usuario,senha))
		users = cursor.fetchall()


		print("OI", users)

		times = False
		if len(users) > 0:
			querySelect = "SELECT * FROM times_coders WHERE usuario=%s"
			cursor.execute(querySelect,(str(users[0][0])))
			print("----------")
			print(users)
			print("----------")
			print(str(users[0][0]))
			times = cursor.fetchall()
			print("----------")
			print(times)
			times = len(times)
			print("----------")
			print(times)
			return True, list(users), times
		else:
			return False, list(users), times

	def busca_time_editar(self,nome):
		cursor = self.conexao.cursor()
		querySelect = "SELECT * FROM times_coders WHERE nome_time=%s"
		cursor.execute(querySelect,(nome))
		time = cursor.fetchall()
		if len(time) > 0:
			return True,list(time)
		else:
			return False,list(time)


	def editarTime(self,nome,membros,id):
		cursor = self.conexao.cursor()
		#cursor.execute("UPDATE carros SET nome_dono = 'Joaquim' WHERE placa = 'ABC-1234'")
		query = "UPDATE times_coders SET nome_time=%s, componentes_grupo=%s WHERE id_time=%s"
		cadastrado = False

		try:
			cursor.execute(query,(nome,membros,id))
			MysqlBanco.count+=1
			self.conexao.commit()
			print("OK, Salvo no banco de dados")
			cadastrado = True
		except:
			print("Erro ao salvar no banco de dados!!!!!")

		return cadastrado
