#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ['A', 'E', 'I', 'O', 'U']

letra = str(input('Por favor, digite uma letra: ')).upper().strip()

if letra in vogal:
    print(f'A letra digitada foi {letra} e é uma VOGAL')
else:
    print(f'A letra digital foi {letra} e é uma CONSOANTE')
