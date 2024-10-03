'''
escola: senai suico brasileiro

titulo: conversao de real para o dolar
autor: ronaldo souza
data: 19 de setembro de 2024
descricao: desenvolver um algoritmo que o valor na moeda real (R$), a cotacao da conversao real paa dolar, e apresente a quantidade desse valor em dolar ($)
exemplo da execucao:
- insirir o valor em real: 5000 reais
- cotacao do dia: 5 dolar
- r$ 5.000 equivale $ 1,000

'''

# entrada de dados
# processamento de dados
# saida de dados

real = 5000
dolar = 5
conversao_dolar = real / dolar
print('5000 reais convertido para a moeda americana é = ', conversao_dolar)
print(f'r$ {real} reais, equivale a $ {conversao_dolar}, na moeda americana')
print('r$ ' + str(real) + ' equivalem $ ' + str(conversao_dolar))