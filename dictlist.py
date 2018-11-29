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
  auxList = []
  for j in range(10): # simulação acontecendo
    auxList.append(j)
  dictValues.setdefault('valorSim%i'%i,[]).append(auxList) # armazenando dados da simulação
print(dictValues)

for key, value in dictValues.items():
  dictResults.setdefault('Media de %s'%key,[]).append(numpy.mean(value)) # armazenando dados da simulação
print(dictResults)