'''
Carlos quer monitorar seu orçamento mensal para evitar gastos 
excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e 
precisa de um programa que ajude a controlar suas despesas. O 
programa deve receber o total de despesas realizadas e informar se ele 
ultrapassou o limite ou ainda está dentro do orçamento.
'''

monthly_budget = 3000.00
total_expenses = float(input("Enter this month's total expenses: "))

if total_expenses > monthly_budget:
    print('You have exceeded your monthly budget')
else:
    print('You are within your monthly budget')