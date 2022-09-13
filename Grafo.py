import graphviz


"""
función generarGrafo

input: 	listaAlu - lista que contiene "alumnos" que a su vez son listas con 4 elementos: id, nombre, amigos y enemigos
	   	dictAmigos - contiene un diccionario en que las llaves con ids de alumnos y los valores son contadores de cuantos otros alumnos tienen esa id como "amigo"

output:	grafo - puede ser un archivo pdf, un svg, png, etc... Es el sociograma/grafo hecho a partir de los alumnos y sus amigos

funcionamiento: recorre listaAlu y dictAmigos en primera instancia para generar los nodos del grafo.
"""

def generarGrafo(listaAlu, dictAmigos):
	dot = graphviz.Digraph(comment='Sociograma', engine='neato', 
		graph_attr={'splines': 'true', 'arrowhead': 'normal', 'overlap': 'false'}, 
		format='png')

	for alumno in listaAlu:
		color = ''
		ancho = 1.0
		if alumno[0] in dictAmigos.keys():
			if dictAmigos[alumno[0]] > 0:
				color = 'green'
				ancho = dictAmigos[alumno[0]]*1.5
			elif dictAmigos[alumno[0]] < 0:
				color = 'red' 
				ancho = -dictAmigos[alumno[0]]*1.5
			else:
				color = 'black'
		else:
			color = 'black'
		dot.node(alumno[0], alumno[1], shape='box', color=color, penwidth=str(ancho)) 

	for alumno in listaAlu:
		for amigo in alumno[2]:
			if isinstance(amigo,str):
				for alumno2 in listaAlu:
					if alumno2[0].upper() == amigo.upper():
						dot.edge(alumno[0],alumno2[0],constraint='false', color='green')
		for enemigo in alumno[3]:
			if isinstance(enemigo,str):
				for alumno2 in listaAlu:
					if alumno2[0].upper() == enemigo.upper():
						dot.edge(alumno[0],alumno2[0],constraint='false', color="red")
	
	dot.render(directory='doctest-output/',filename='sociograma.gv').replace('\\', '/') 