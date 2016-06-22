import random
# Se utilizara Representacion Binaria
#Cada individuo es una posible solucion al problema.

class A_Genetic:
	num_fil            = 2
	num_aulas          = 0   # Num Aulas, seran mis objetos que puedo elegir 
	longitud_cromosoma = 0   # Numero de genes por cadena
	num_individuos_pob = 0   # Numero de individuos en la poblacion
	capacidad_mochila  = 0   # Capacidad de aulas de un colegio
	poblacion          = []  # Matriz en la cual cada fila representa un individuo o cromosoma
	peso_beneficio     = []  # Matriz que contiene en la primera fila los pesos y en la segunda fila su beneficio
	list_result_fitnes = []  # Lista en la que guardare resultados que retora la funcion al evaluar al individuo
	var_K              = 0   # Variable que se utiliza para la funcion fitness
	def __init__(self,capacidad_mochila,var_K,num_indi,long_cromo):
		self.capacidad_mochila = capacidad_mochila
		self.var_K             = var_K
		self.num_individuos_pob= num_indi
		self.longitud_cromosoma= long_cromo
	def setPesosBeneficios(self):
		for  i  in range(self.num_fil):
			self.peso_beneficio.append([])
			for j in range(self.num_individuos_pob):
				if i == 0:
					peso = random.randint(20,40)  # Entre 20 y 40 el num de alumnos
					print 'Pesos', peso
					self.peso_beneficio[i].append(peso)   # Pesos de acuerdo al numero de alumnos por clase entre 20 y 40 
				else:
					beneficio = random.randint(20,100) # El beneficio va entre 20 y 100
					print 'Beneficio',beneficio
					self.peso_beneficio[i].append(beneficio)
	
	def generarPoblacion(self):
		for x in range(self.num_individuos_pob):
			self.poblacion.append([])
			for y in range(self.longitud_cromosoma):
				gen = random.randint(0,1)  # Gen entre 0 y 1 
				self.poblacion[x].append(gen)


	def evaluar (self,peso,beneficio,var_X):
		evaluacion =  peso*var_X
		if evaluacion <= self.capacidad_mochila:
			evaluacion = 0
		else:
			evaluacion  = evaluacion - self.capacidad_mochila
		return beneficio-var_X - self.var_K * (evaluacion)

	def funcionFitness(self,list_temp_indi):
		size = len(list_temp_indi)
		fitness = 0
		for j in range(self.longitud_cromosoma):    #Recorro el cromosoma
			# Solo evaluo si el gen es 1 porq qiere decir q ese objeto estoy eligiendo para llevar
			if list_temp_indi[j] == 1:
				fitness = fitness + self.evaluar( self.peso_beneficio[0][j],self.peso_beneficio[1][j],list_temp_indi[j])
		#Agrego a mi lista de resultados el resultado de cada inidividuo
		self.list_result_fitnes.append(fitness)
		
	
	#Ordenar a todos los individuos segun su funcion Fitness ascendentemente
	def seleccionRanking(self):
		for x in range(self.num_individuos_pob):
			print self.poblacion[x]
			self.funcionFitness( self.poblacion[x] )

		# Como en la lista `list_result_fitness` tengo todos los resultados de una poblacion
		# Solo me queda ordenar esa lista y tengo mi Ranking
		self.list_result_fitnes.sort() 
		print "\n\n SELECCION POR RANKIG RESULTADOS"
		print self.list_result_fitnes

def main():
	Obj = A_Genetic(40,7,6,5)        # Le paso la capacidad de la mochila y var_K, num individuos, longitud cromosoma
	Obj.generarPoblacion()  
	Obj.setPesosBeneficios()  # Pesos y beneficios para el total num de individuos
	Obj.seleccionRanking()

main()
