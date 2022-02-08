#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
#mês.Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

hora = float(input('Quanto você ganha por hora? R$ '))
horames = int(input('Quantas horas você trabalhou este mês? '))
salariob = hora * horames
ir = salariob * 11 / 100
inss = salariob * 8 / 100
sindicato = salariob * 5 / 100
salariol = salariob - ir - inss - sindicato
#salário bruto.
print(f'Seu salário bruto é de R${salariob:.2f}')
#quanto pagou ao INSS.
print(f'O valor pago referente a INSS foi de R${inss:.2f}')
#quanto pagou ao sindicato.
print(f'O valor pago ao sindicato foi de R${sindicato:.2f}')
print(f'Seu salario líquido é de R${salariol:.2f}')