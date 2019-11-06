import time

a = int(input())
b = int(input())
timeINI = time.clock()

print("Soma = ",a+b)
print("Mult = ",a*b)
print("Sub = ",a-b)
print("Div = ",a/b)

timeFIM = time.clock()
#print("TEMPO Segundos: ", timeFIM- timeINI)
#print("TEMPO mili: ", (timeFIM- timeINI)*1000)