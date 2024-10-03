# escola: senai suico brasileiro

# titulo: conversao de unidade
# autor: ronaldo souza
# data: 24 de setembro de 2024

# faça um programa que recebe um numero em
# pes, faça a conversoes e a seguir mostre os resultados
# - polegadas; --->> 1 pe = 12 polegadas
# - jardas; --->> 1 jarda = 3 pes
# - milhas; --->> 1 milha = 1.760 jardas

#entrada de dados
pes = int(input('digite o valor em pes: '))

# processamento
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760

# saida
print('polegadas:', polegadas)
print('jardas:', jardas)
print('milhas:', milhas)
print('')
print(pes, 'pes, equivale a: ', polegadas, 'polegadas')
print(pes, 'pes, equivale a: ', jardas, 'jardas')
print(pes, 'pes, equivale a: ', milhas, 'milhas')