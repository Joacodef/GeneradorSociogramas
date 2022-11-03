import graphviz


"""
función:	 	generarGrafo

parámetros: 	listaAlu	list	lista que contiene "alumnos" que a su vez son listas con 4 elementos: id, nombre, amigos y enemigos
	   			dictAmigos	dict	contiene un diccionario en que las llaves con ids de alumnos y los valores son contadores de cuantos otros alumnos tienen esa id como "amigo"

output:			grafo 	graphviz.Digraph	puede ser un archivo pdf, un svg, png, etc... Es el sociograma/grafo hecho a partir de los alumnos y sus amigos

explicación: 	recorre listaAlu y dictAmigos en primera instancia para generar los nodos del grafo. Luego genera los arcos.
"""

def generarGrafo(listaAlu, dictAmigos):
	dot = graphviz.Digraph(comment='Sociograma', engine='neato',
		graph_attr={'splines': 'true', 'arrowhead': 'normal', 'overlap': 'false','mode':'sgd'},
		format='png') 
		#modes (con neato): KK, sgd(el mejor hasta ahora), major, hier, ipsep)
		#engines: fdp, circo

	for alumno in listaAlu:
		color = ''
		ancho = 1.0
		if alumno[0] in dictAmigos.keys():
			popularidad = dictAmigos[alumno[0]]
			if popularidad > 0:
				color = 'chartreuse1'
				ancho = popularidad*1.5
			elif popularidad < 0:
				color = 'brown1' 
				ancho = -popularidad*1.5
			else:
				color = 'black'
		else:
			color = 'black'
		if str(alumno[0]) == "-1": continue
		print("Nodo a crear: id - "+str(alumno[0])+", nombre - "+str(alumno[1])+", color - "+str(color)+", ancho - "+str(ancho)+", popularidad - "+str(popularidad)) 
		dot.node(alumno[0], alumno[1], shape='box', color=color, penwidth=str(ancho))
		

	for alumno in listaAlu:
		for amigo in alumno[2]:
			if isinstance(amigo,str):
				for alumno2 in listaAlu:
					if alumno2[0].upper() == amigo.upper():
						dot.edge(alumno[0],alumno2[0],constraint='false', color='chartreuse3')
		for enemigo in alumno[3]:
			if isinstance(enemigo,str):
				for alumno2 in listaAlu:
					if alumno2[0].upper() == enemigo.upper():
						dot.edge(alumno[0],alumno2[0],constraint='false', color="brown3")
	
	dot.render(directory='doctest-output/',filename='sociograma').replace('\\', '/') 