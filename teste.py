"""
from my_math import area_quad, area_ret, peri_quad
import math

print(area_quad(5))
print(area_ret(5, 10))
print(peri_quad(10))

print(math.factorial(5))
print(math.sqrt(25))
"""
texto = '''Machine learning

	- Aprendendo Python
	
		Python é muito legal!!!
'''
    
arq = open('arquivo.txt', 'w')
arq.write('Machine learning\n')
arq.write('- Aprendendo Python\n')
arq.write(texto)
arq.close()

# ou

with open('arquivo.txt', 'w') as f:
	f.write(texto)
	

with open('dataset.txt', 'r') as arq:
#	for linha in arq.readlines():
#		print(linha)
## ou
#	conteudo = arq.read()
#	print(conteudo)
## ou
	lista = arq.read().splitlines()
	print(lista[0])

print(len(lista))
	"""
