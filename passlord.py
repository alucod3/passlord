import random

print('\033[0;35m█ ▄▄  ██      ▄▄▄▄▄    ▄▄▄▄▄   █    ████▄ █▄▄▄▄ ██▄   ')
print('\033[0;35m█   █ █ █    █     ▀▄ █     ▀▄ █    █   █ █  ▄▀ █  █  ')
print('\033[0;35m█▀▀▀  █▄▄█ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄   █    █   █ █▀▀▌  █   █ ')
print('\033[0;35m█     █  █  ▀▄▄▄▄▀   ▀▄▄▄▄▀    ███▄ ▀████ █  █  █  █  ')
print('\033[0;35m █       █                         ▀        █   ███▀  ')
print('\033[0;35m  ▀     █                                  ▀          ')
print('\033[0;35m       ▀                                              ')

print('P4sSl0Rd Ver. v1.00.00')
print('Coded by alucod3')

min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '!@#$%*()[];.,<>/-'

qnt = input('\n \033[;1m -> Digite a quantidade de caracteres: ')
qntInt = int(qnt)
length = qntInt

#fazendo senha com todos
all = min + max + num + sybs
passwordAll = "".join(random.sample(all,length))

#só maiúsculas e números
MAXnum = max + num
passwordMAXnum = "".join(random.sample(MAXnum,length))

#só minusculas e maiúsculas
MAXmin = max + min
passwordMAXmin = "".join(random.sample(MAXmin,length))

print ('\n')
print ('\033[1;31mPassword ALL ---------> ' + passwordAll.strip())
print ('\033[1;31mPassword UPPER_NUM ---> ' + passwordMAXnum.strip())
print ('\033[1;31mPassword UPPER_LOWER -> ' + passwordMAXmin.strip())
