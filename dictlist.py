# Organização de dados em dicionários com listas
# Cada dicionário vai ter uma chave que informa o tipo de dado que esta sendo armazenado
# Para simulação, cada chave segura uma lista que, para cada item nela é um resultado da simulação
# Chave x: Valor 1 - Simulação 1
# Chave x: Valor 2 - Sumulação 2
# ...

import numpy

dictValues = {}
dictResults = {}
for i in range(10): # número de simulações
  auxList1 = [] # tipos de dados que serão armazenados
  auxList2 = [] # para serem usados para a análise estatística
  auxList3 = [] # das simulações
  for j in range(10): # simulação acontecendo
    auxList1.append(j)
    auxList2.append(j+10)
    auxList3.append(20+j)
  # armazenando dados da simulação
  dictValues.setdefault('valorSim%i'%i,{}).setdefault('Dado1',[]).extend(auxList1)
  dictValues.setdefault('valorSim%i'%i,{}).setdefault('Dado2',[]).extend(auxList2)
  dictValues.setdefault('valorSim%i'%i,{}).setdefault('Dado3',[]).extend(auxList3)
# print(dictValues)

for key, value in dictValues.items(): # armazenando dados de avaliação da simulação
  print("Key: ", key, "\tValue: ", value)
  # dictResults.setdefault('Media de %s'%key,[]).append(numpy.mean(value))
# print(dictResults)