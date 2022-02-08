#Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número é o {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior número é o {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior número é o {n3}')


