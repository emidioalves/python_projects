"""
Este é o módulo nested.py, e fornece uma função chamada print_lol()
que imprime listas que podem ou não estarem aninhadas
"""

"""
Esta função requer um argumento posicional chamado "the_list" 
que é qualquer lista Python (de possiveis listas aninhadas). Cada item 
na lista fornecida é (recursivamente) impresso em sua própia linha
"""
def printerlol(each_item):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)
	
	