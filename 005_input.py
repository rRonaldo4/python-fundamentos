# escola: senai suico brasileiro

# titulo: conversao de real para o dolar
# autor: ronaldo souza
# data: 24 de setembro de 2024

# descricao: desenvolver um algoritmo onde 
# o usuario digita o valor na moeda real (R$), 
# a cotacao da conversao real paa dolar, e apresente 
# a quantidade desse valor em dolar ($)
# exemplo da execucao:
# - insirir o valor em real: 5000 reais
# - cotacao do dia: 5 dolar
# - r$ 5.000 equivale $ 1,000

 
 
 
# entrada de dados
moeda_real_string= input('insira o valor em real: ')
cotacao_dia_string= input('insira o valor da cotação: ')

# processamento
moeda_real = int(moeda_real_string)
cotacao_dia = int(cotacao_dia_string)
moeda_dolar = moeda_real / cotacao_dia

# saida
print(f'r$ {moeda_real} reais , equivales a $ {moeda_dolar}')