nome='Luiz Otavio'
altura= 1.80
peso=95
imc = peso/(altura*altura)

"f-strings"
linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso}kg e seu IMC e'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)