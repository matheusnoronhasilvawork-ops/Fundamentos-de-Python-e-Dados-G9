'''
Você está recebendo uma lista de valores representando os produtos de 
sua loja virtual e gostaria de calcular a soma total desses produtos para 
entender o desempenho financeiro semanal.
'''

values = [10, 20, 30, 40, 50]

total_sum = 0

for value in values:
    total_sum += value

print(f"The total sum of the values is: {total_sum}")