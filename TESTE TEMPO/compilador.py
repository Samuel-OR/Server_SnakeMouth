import os
import time

#nome = input("Digite um nome do arquivo: ")
nome = "exercicio.py"
tempoLimite = 0.5

# ERRO  DE EXECUÇÃO
# VERIFICAR ALGUMA ANOMALIA NA RESPOSTA

timeINI = time.clock()
os.system("nohup python3 {} < entradaPROF.txt > saidaAPRES.txt".format(nome))
timeFIM = time.clock()

print("TEMPO Segu: ", timeFIM- timeINI)
print("TEMPO mili: ", (timeFIM- timeINI)*1000000)

saidaAPRES = open('saidaAPRES.txt', 'r')
saidaAPRES = (saidaAPRES.readlines())
saidaAPRES = ' '.join(saidaAPRES)

if("Traceback" in saidaAPRES or "NameError" in saidaAPRES):
	print("ERRO DE SINTAXE")
else:
	# ESTOURO DE TEMPO     (ESTOURO  TEMPO)

	if(((timeFIM- timeINI)*1000) > tempoLimite):
		print("ESTOURO DE TEMPO.")
	else:
		
		os.system("python3 {} < entradaPROF.txt > saidaBRUTO.txt".format(nome))
		#CONV'ERTENDO ARQUIVO NUMA LISTA
		saidaPROF = open('saidaPROF.txt', 'r')
		saidaPROF = (saidaPROF.readlines())
	
		saidaBRUTO=open('saidaBRUTO.txt', 'r')
		saidaBRUTO = (saidaBRUTO.readlines())
	
		if saidaPROF == saidaBRUTO:
			print("RESPOSTA CORRETA")
		else:
			#VERIFICAR ERRO DE APRESENTAÇÃO
				#-i = remove case sentitive
				#-w = Ignora espaços em branco
				#-b = Ignore as mudanças na quantidade de espaço em branco.
				#-B = Ignore as alterações cujas linhas estão todas em branco.	
			os.system("diff -b -B -w -i saidaPROF.txt saidaBRUTO.txt > resulEXEC.txt")
			resulEXEC = open('resulEXEC.txt', 'r')
	
			if(len(resulEXEC.readlines())==0):
				print("ERRO DE APRESENTAÇÃO")
			else:
				print("RESPOSTA INCORRETA")
			os.system("rm resulEXEC.txt")
		os.system("rm saidaBRUTO.txt")
os.system("rm saidaAPRES.txt")
