frase = str(input('digite uma frase: ').lower())
fra = frase.strip()
totala = frase.count('a')
az = fra.rfind('a')
aa = fra.find('a')
print(f'a frase tem {totala} de letras a')
print(f'o primeiro a está na posição {aa + 1}')
print(f'o ultimo a está na posicao {az+1}')
