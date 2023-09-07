""" Escreva um programa que leia um número inteiro qualquer e peça para o usúario escolher qual será a base de conversão
> 1 para BINÁRIO
> 2 para OCTAL
> 3 para HEXADECIMAL
 """
from time import sleep

num = int(input('Digite um número para converção: '))
print('''Escolha umas das bases para a conversão:
[ \33[0:31m1\33[m ] converter para \33[0:31mBINÁRIO\33[m
[ \33[0:31m2\33[m ] converter para \33[0:31mOCTAL\33[m
[ \33[0:31m3\33[m ] converter para \33[0:31mHEXADECIMAL\33[m''')
opcao = int(input('\33[0:32mDigite sua opção\33[m: '))
print('\33[0:33mCARREGANDO INFORMAÇÃO\33[m...')
sleep(3)
if opcao == 1:
    print('O número \33[0:36m{}\33[m Convertido para \33[0:36mBINÁRIO\33[m é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número \33[0:36m{}\33[m Convertido para \33[036mOCTAL\33[m é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número \33[0:36m{}\33[m Convertido para \33[0:36mHEXADECIMAL\33[m é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\33[0:41mOpção Invalida!\33[m')
