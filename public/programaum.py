import random
from time import sleep
print('='*30)
print('{:^30}'.format('PROGRAMA UM'))
print('='*30)
while True:
	menu1 = input('''
Olá, escolha uma opção para continuar:
[ 1 ] Jogo da Advinhação
[ 2 ] Calculadora
''')
	sleep(0.5)
	print('Carregando...\n')
	sleep(0.5)
	if menu1 == '1':
		print ('='*30)
		print('{:^30}'.format('JOGO DA ADIVINHAÇÃO'))
		print ('='*30)
		while True:
			npc = random.randint(0, 10)
			count = 0
			while True:
				njog = input('''
Adivinhe o número que estou pensando entre 0 e 10: 
''')
				if not njog.isdigit():
					print('\033[1;31mDigite apenas números entre 0 e 10 \033[0;0m')
				if njog.isdigit():
					njog = int(njog)
					if njog > 10:
						print('\033[1;31mDigite apenas números entre 0 e 10 \033[0;0m ')
					elif njog < npc:
						print('\n\033[1;031mErrou... \033[0;0mtente um número maior')
						sleep(0.5)
					elif njog > npc:
						print('\n\033[1;031mErrou... \033[0;0m tente um número menor')
						sleep(0.5)
					elif njog == npc:
						print('\n\033[1;32mAcertou!\033[0;0m')
						print (f'Você precisou de {count} tentativa(s)')
						sleep(0.5)
						break
					count += 1
			replay = str(input('''
Deseja continuar?
[ 1 ] Continuar Jogando
[ 2 ] Voltar ao menu inicial 
'''))
			if replay == '2':
				sleep(0.5)
				print('''
Finalizando...

''')
				print('='*30)
				sleep(0.5)
				break
			if replay =='1':
				continue
			while replay != '1' and replay != '2':
				print('Escolha uma das opções')
	if menu1 == '2':
		print ('='*30)
		print('{:^30}'.format('CALCULADORA'))
		print ('='*30)
		print ('\n\033[;031mNão estou pronta, volte mais tarde ;D\033[0;0m\n')
		sleep(1)
		print('='*30)
		