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

	def cadastrarTime(self,nomeTime,membros):

		cursor = self.conexao.cursor()
		query = "INSERT INTO times_coders(nome_time,componentes_grupo) VALUES(%s,%s)"
		cadastrado = False

		try:
			cursor.execute(query,(nomeTime,membros))
			MysqlBanco.count+=1
			self.conexao.commit()
			print("OK, Salvo no banco de dados")
			cadastrado = True
		except:
			print("Erro ao salvar no banco de dados!!!!!")

		return cadastrado


	def verifica_login(self,usuario,senha):

		querySelect = "SELECT * FROM pro WHERE email=%s AND passwd=%s"
		cursor.execute(querySelect,(email,passwds))
		users = cursor.fetchall()

