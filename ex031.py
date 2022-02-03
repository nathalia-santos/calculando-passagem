#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = int(input('Qual será a distância, em KM, da sua viagem? '))

if km <= 200:
    valor = 0.50 * km
    print(f'Sua passagem custará R${valor:.2f}')
else:
    valor = 0.45 * km
    print(f'Sua passagem custará R${valor:.2f}')

