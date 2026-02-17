'''
Fernanda está planejando uma viagem e quer calcular quanto pagará de 
pedágio. O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00

Crie um programa que receba a distância percorrida e informe o valor 
do pedágio correspondente.
'''

distance = float(input("Digite a distância percorrida em km: "))

if distance <= 100:
    toll_fee = 10.00
elif distance <= 200:
    toll_fee = 20.00
else:
    toll_fee = 30.00

print(f"O valor do pedágio é R$ {toll_fee:.2f}")