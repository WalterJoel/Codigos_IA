import random
# Se utilizara Representacion Binaria
#Cada individuo es una posible solucion al problema.

class A_Genetic:
	iteraciones        = 0
	porcentaje_mutacion= 0.0
	num_fil            = 2
	num_aulas          = 0   # Num Aulas, seran mis objetos que puedo elegir 
	longitud_cromosoma = 0   # Numero de genes por cadena
	num_individuos_pob = 0.0   # Numero de individuos en la poblacion
	capacidad_mochila  = 0   # Capacidad de aulas de un colegio
	poblacion          = []  # Matriz en la cual cada fila representa un individuo o cromosoma
	peso_beneficio     = []  # Matriz que contiene en la primera fila los pesos y en la segunda fila su beneficio
	list_result_fitnes = []  # Lista en la que guardare resultados que retora la funcion al evaluar al individuo
	var_K              = 0   # Variable que se utiliza para la funcion fitness
	def __init__(self,capacidad_mochila,var_K,num_indi,long_cromo,percent,num_iter):
		self.iteraciones         = num_iter
		self.capacidad_mochila   = capacidad_mochila
		self.var_K               = var_K
		self.num_individuos_pob  = num_indi
		self.longitud_cromosoma  = long_cromo
		self.porcentaje_mutacion = percent
	#En la matriz peso beneficio agrego en la fila 1 el peso y en la fila 2 el beneficio
	def setPesosBeneficios(self):
		for  i  in range(self.num_fil):
			self.peso_beneficio.append([])
			for j in range(self.num_individuos_pob):
				if i == 0:
					peso = random.randint(20,40)  # Entre 20 y 40 
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
		#Recorro todos los individuos
		for x in range(self.num_individuos_pob):
			#print self.poblacion[x]
			self.funcionFitness( self.poblacion[x] )

		# Como en la lista `list_result_fitness` tengo todos los resultados de una poblacion
		# Solo me queda ordenar esa lista y tengo mi Ranking
		self.list_result_fitnes.sort() 
		print "\n\n SELECCION POR RANKIG RESULTADOS"
		print self.list_result_fitnes
	#Conservar los mejores de una poblacion
	def Mutacion(self):	
		#Calculo la cantidad de genes que voy a mutar segun el porcentaje
		cant_mutar = 0.0
		cont       = 0
		cant_mutar = (self.porcentaje_mutacion*self.num_individuos_pob) / 100.0
		#print self.poblacion
		#print "a mutar"
		#print cant_mutar
		pos_random_indiv = random.randint(0,self.num_individuos_pob-1) #Porque los individuos estan en la matriz poblacion
		while cont < cant_mutar:
			#ELige la posicion random entre las pos 0 y el num_individuos
			pos_random_gen   = random.randint(0,self.longitud_cromosoma-1) #Randon para el gen del individuo
			#Cambio el gen 
			if self.poblacion[pos_random_indiv][pos_random_gen] == 0:
				self.poblacion[pos_random_indiv][pos_random_gen] = 1
			else :
				self.poblacion[pos_random_indiv][pos_random_gen] = 1
			cont = cont + 1
		#print self.poblacion
		
	def Cruzamiento(self):
		#Escogemos aleatoriamente dos individuos, padre y madre :)
		indiv1 = 0
		indiv2 = 0
		# Para que el individuo no sea el mismo
		while indiv1==indiv2:
			indiv1 = random.randint(0,self.num_individuos_pob-1) #Porque los individuos estan en la matriz poblacion
			indiv2 = random.randint(0,self.num_individuos_pob-1) #Randon para el gen del individuo
		#Ahora elijo una posicion K para el cruzamiento, a partir de alli hago el cruce
		pos_k = random.randint(1,self.longitud_cromosoma-1)
		cont = 0
		list_temp_padre = []
		list_temp_madre = []
		#print "PADRES"
		#print "pos_k: ",pos_k
		#print self.poblacion[indiv1]
		#print self.poblacion[indiv2]
		indice1 = self.Count_Unos( self.poblacion[indiv1])
		indice2 = self.Count_Unos( self.poblacion[indiv2])

		#Itero hasta la pos k
		while cont < pos_k:
			list_temp_padre.append(self.poblacion[indiv1][cont])
			list_temp_madre.append(self.poblacion[indiv2][cont])
			cont = cont + 1
		# Ahora cont = K
		cont = pos_k
		while cont < self.longitud_cromosoma:
			#Aqui invierto las colas del indiv1 al indiv2
			list_temp_padre.append(self.poblacion[indiv2][cont])
			list_temp_madre.append(self.poblacion[indiv1][cont])
			cont = cont + 1
		#Ahora ya solo queda agregar el cr
		#******************* APLICANDO ELITISMO ******************************
		# Si despues de hacer cruzamiento, el hijo es mejor lo coloco, sino dejo el anterior
		indice3 = self.Count_Unos(list_temp_padre)
		if  indice3 > indice1:
			self.poblacion[indiv1] = list_temp_padre
		indice4 = self.Count_Unos(list_temp_madre)
		if  indice4 > indice2:
			self.poblacion[indiv2] = list_temp_madre

		
		#print "HIJOS"
		#print self.poblacion[indiv1]
		#print self.poblacion[indiv2]
	def Remove_List(self):
		for x in self.list_result_fitnes[:]:
			self.list_result_fitnes.remove(x)
	def Count_Unos(self,list_a):
		cont = 0
		for x in range(self.longitud_cromosoma):
			if list_a[x] == 1:
				cont = cont+1
		return cont
	
	#Las iteraciones
	def Bucle(self):
		self.generarPoblacion()
		self.setPesosBeneficios()
		print "Poblacion 0: *****"
		self.seleccionRanking()
		cont = 1
		while cont<self.iteraciones:
			#limpio la lista del ranking
			self.Remove_List()
			self.Cruzamiento()
			self.Mutacion()
			print "Poblacion: ",cont, " *****"
			self.seleccionRanking()
			
			cont = cont+1


def main():
	Obj = A_Genetic(40,7,10,5,10,7)        # Le paso la -- capacidad de la mochila, var_K, num individuos, longitud cromosoma, porcentaje mutacion,veces q itero
	Obj.Bucle()
main()