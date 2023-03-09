"""01 - Receber 3 variáveis que representam as notas de um aluno e verificar se o aluno está aprovado ou reprovado, 
mostrar a situação na tela. O aluno estará aprovado caso a média seja maior ou igual a 7.0. Fórmula:
(nota1 + nota2 + nota3)/3"""

def media(nota1,nota2,nota3):
	m = (nota1+nota2+nota3)/3
	if m >= 7:
		print (f'o aluno esta aprovado com uma media igual a {m}')
	else:
		print(f'o aluno esta reprovado com uma media igual a {m}')
		
		

"""02 - Realizar a mesma tarefa do exercício 01, fazendo calculo de 10 alunos. Receber uma lista com as notas 1,
 lista com as notas 2 e lista com as notas 3 e exibir a situação dos alunos."""

def media_alunos(notas1, notas2, notas3):
	for i in range(len(notas1)):
		notas = (notas1[i]+notas2[i]+notas3[i])/3
		j = str(i+1)
		if notas >= 7:
			print(f'aluno{j} esta aprovado com uma media igual a {notas}')
		else:
			print(f'aluno{j} esta reprovado com uma media igual a {notas}')



"""03 - Crie uma lista com os 1000 primeiros numeros e separe-os em outras duas listas: uma com os números pares e outra com os ímpares."""


numeros = []
numerospar =[]
numerosimpar = []
	
for i in range(0,1001):	
	numeros += [i]
	
	if i % 2 == 1:
		numerosimpar += [i]
			
	elif i % 2 == 0:
		numerospar += [i]


'''03 -Dê a soma de todos os números primos menores que 1000'''

def somaprimo():
	primos = []
	for i in range(len(numeros)):
		teste = []
		if numeros[i] == 0 or numeros[i] == 1:
			pass
		else:
			for j in range(len(numeros)):
						if numeros[j] == 0 or numeros[j] == 1:
							pass
						elif numeros[i] % numeros[j] == 0:
								teste += [i]
		if len(teste) ==1:
			primos += [i]
	
	print('soma dos numeros primos:'+str(sum(primos)))


media(1,8,9)
media_alunos([1,5,8,2,6,2,7,4,7,4],[4,7,3,9,6,5,7,5,7,3],[1,2,4,8,9,6,4,6,3,5])
somaprimo()