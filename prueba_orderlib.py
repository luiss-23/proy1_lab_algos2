"""
orderlib.py

Autores: Luis Carlos Blanco, 17-10066
         Gabriel Chaurio, 17-10164

Descripcion: Este programa buscara el timepo promedio de ejecucion de los algoritmos 
de ordenamiento implementados en orderlib.py

Ultima modificacion: 17/02/2020
"""
import random, argparse, time, matplotlib, statistics, sys
from orderlib import *
import numpy as np
import graficar_puntos as gp
sys.setrecursionlimit(10000000)


def punto_flotante(n:int) -> list:
	a = []

	for i in range(n):
		a.append(random.random())

	return a 


def ordenado(n:int) -> list:
	a = []

	for i in range(n):
		a.append(random.randint(0,n))
	
	a.sort()

	return a 

def orden_inverso(n:int) -> list:
	a = []

	for i in range(n):
		a.append(random.randint(0,n))

	list.reverse(a)

	return a

def cero_uno(n:int) -> list:
	a = [] 

	for i in range(n):
		a.append(random.randint(0,1))

	return a 

def mitad(n:int) -> list:
	a = []

	for i in range(1,n//2):
		a.append(i)

	for j in range(n//2,0,-1):
		a.append(j)

	return a 

def casi_ord_1(n:int) -> list:
	if(n < 8):
		print('La lista debe tener al menos 32 elementos')
	else: 
		a = ordenado(n)
		print(a)
		for i in range(0,n-8):
			a[i], a[i+8] = a[i+8], a[i]

	return a

def casi_ord_2(n:int) -> list:
	if(n < 4):
		print('La lista debe tener al menos 32 elementos')
	else: 
		a = ordenado(n)

		for i in range(0,n-4):
			a[i], a[i+4] = a[i+4], a[i]

	return a

#Seleccion del tipo de arreglo
#r: tipo de secuencia que se introduce al iniciar el programa
#k: numero de elementos que tendra la secuencia e intervalo 
#en el cual saldran los numeros
def type_arr(r,k:int) -> [int]:
	arr = []

	if r == 1:
		arr = punto_flotante(k)
	elif r == 2:
		arr = ordenado(k)
	elif r == 3:
		arr = orden_inverso(k)
	elif r == 4:
		arr = cero_uno(k)
	elif r == 5:
		arr = mitad(k)
	elif r == 6:
		arr = casi_ord_1(k)
	elif r == 7:
		arr = casi_ord_2(k)

	return arr

#Medicion de los tiempos
#a: arreglo que va a ser ordenado
def estudio_tiempo(a,mer,quit,qui,med,intr,quw3,dual,tim:list) -> [int]:


	cop_arr = a[:]
	#Medicion selection_sort
	ti1 = time.perf_counter()
	mergesort(cop_arr)
	tf1 = time.perf_counter() - ti1
	mer.append(tf1)

	cop_arr = a[:]
	#Medicion shell_sort
	ti2 = time.perf_counter()
	quicksort_it(cop_arr)
	tf2 = time.perf_counter() - ti2
	quit.append(tf2)

	cop_arr = a[:]
	#Medicion bubble_sort
	ti3 = time.perf_counter()
	quicksort(cop_arr,0,len(cop_arr)-1)
	tf3 = time.perf_counter() - ti3
	qui.append(tf3)

	cop_arr = a[:]
	#Medicion insertion_sort
	ti4 = time.perf_counter()
	median_of_3_quicksort(cop_arr,0,len(cop_arr))
	tf4 = time.perf_counter() - ti4
	med.append(tf4)

	cop_arr = a[:]
	#Medicion del mergesort
	ti5 = time.perf_counter()
	introsort(cop_arr,0,len(cop_arr))
	tf5 = time.perf_counter() - ti5
	intr.append(tf5)

	cop_arr = a[:]
	#Medicion del mergesort_insertion
	ti6 = time.perf_counter()
	quicksort_w_3_way_partitioning(cop_arr,0,len(cop_arr)-1)
	tf6 = time.perf_counter() - ti6
	quw3.append(tf6)

	cop_arr = a[:]
	#Medicion del mergesort_iterative
	ti7 = time.perf_counter()
	dual_pivot_quicksort(cop_arr,0,len(cop_arr)-1)
	tf7 = time.perf_counter() - ti7
	dual.append(tf7)

	cop_arr = a[:]
	#Medicion del heapsort
	ti8 = time.perf_counter()
	timsort(cop_arr)
	tf8 = time.perf_counter() - ti8
	tim.append(tf8)

	return mer, quit, qui, med, intr, quw3, dual, tim

if __name__ == "__main__":
	#Manejo de los argumentos de entrada del programa
	analyzer = argparse.ArgumentParser(description='Analiza el tiempo de corrida de algoritmos de ordenamiento')
	analyzer.add_argument('-i', type=int, help='Numero de veces que se ejecutara la prueba sobre los algoritmos')
	analyzer.add_argument('-t', type=int, help='Tipo de secuencia a seleccionar')
	analyzer.add_argument('-g', type=bool, help='Indica si se hara una grafica del estudio del tiempo')
	analyzer.add_argument('input', nargs='+')
	arg = analyzer.parse_args()
	ele = []
	ele.extend(arg.input)

	for i in range(0,len(ele)):
		ele[i] = int(ele[i])

	#Variables para almacenar los argumentos de llamada 
	if arg.i:
		i = arg.i
	else:
		i = 3

	if arg.t:
		t = arg.t
	else:
		t = 1

	if arg.g:
		g = True
	else:
		g = False

	#Arreglos para almacenar los promedios 
	pr_mer = []
	pr_quit = []
	pr_qui = []
	pr_med = []
	pr_intr = []
	pr_quw3 = []
	pr_dual = []
	pr_tim = []

	for k in range(0,len(ele)):
		print('Cantidad de elementos = ' +str(ele[k]) +'\n')
		#Arreglos para almacenar el tiempo
		merge = []
		quit = []
		quick = []
		median = []
		intro = []
		quickw = []
		dual = []
		tims = []
		
		for j in range(i):

			lst = type_arr(t, ele[k])
			estudio_tiempo(lst,merge,quit,quick,median,intro,quickw,dual,tims)

		prom_mer = statistics.mean(merge)
		pr_mer.append(round(prom_mer,2))	
		des_mer = statistics.stdev(merge)
		print('El promedio para el algoritmo MergeSort es: ' +str(round(prom_mer,2)) +' segundos, con: ' +str(round(des_mer,2)) +' de STD' +'\n')

		prom_quit = statistics.mean(quit)
		pr_quit.append(round(prom_quit,2))	
		des_quit = statistics.stdev(quit)
		print('El promedio para el algoritmo QuickSort-Iterative es: ' +str(round(prom_quit,2)) +' segundos, con: ' +str(round(des_quit,2)) +' de STD' +'\n')

		prom_qui = statistics.mean(quick)
		pr_qui.append(round(prom_qui,2))	
		des_qui = statistics.stdev(quick)
		print('El promedio para el algoritmo QuickSort es: ' +str(round(prom_qui,2)) +' segundos, con: ' +str(round(des_qui,2)) +' de STD' +'\n')

		prom_med = statistics.mean(median)
		pr_med.append(round(prom_med,2))	
		des_med = statistics.stdev(median)
		print('El promedio para el algoritmo Median-of-3-QuickSort es: ' +str(round(prom_med,2)) +' segundos, con: ' +str(round(des_med,2)) +' de STD' +'\n')

		prom_intr = statistics.mean(intro)
		pr_intr.append(round(prom_intr,2))	
		des_intr = statistics.stdev(intro)
		print('El promedio para el algoritmo IntroSort es: ' +str(round(prom_intr,2)) +' segundos, con: ' +str(round(des_intr,2)) +' de STD' +'\n')

		prom_quw3 = statistics.mean(quickw)
		pr_quw3.append(round(prom_quw3,2))	
		des_quw3 = statistics.stdev(quickw)
		print('El promedio para el algoritmo QuickSort-W-3-Way-Partitioning es: ' +str(round(prom_quw3,2)) +' segundos, con: ' +str(round(des_quw3,2)) +' de STD' +'\n')

		prom_dual = statistics.mean(dual)
		pr_dual.append(round(prom_dual,2))	
		des_dual = statistics.stdev(dual)
		print('El promedio para el algoritmo Dual-Pivot-QuickSort es: ' +str(round(prom_dual,2)) +' segundos, con: ' +str(round(des_dual,2)) +' de STD' +'\n')

		prom_tim = statistics.mean(tims)
		pr_tim.append(round(prom_tim,2))	
		des_tim = statistics.stdev(tims)
		print('El promedio para el algoritmo TimSort es: ' +str(round(prom_tim,2)) +' segundos, con: ' +str(round(des_tim,2)) +' de STD' +'\n')

	if (g == True and len(ele) < 2):
		print('Deben haber al menos dos tamanos de secuencia')
		sys.exit()

	elif(g == True and len(ele) >= 2):
		gp.dibujar_grafica(ele, pr_mer, "MergeSort")
		gp.dibujar_grafica(ele, pr_quit, "QuickSort-Iterative")
		gp.dibujar_grafica(ele, pr_qui, "QuickSort")
		gp.dibujar_grafica(ele, pr_med, "Median-of-three-QuickSort")
		gp.dibujar_grafica(ele, pr_intr, "IntroSort")
		gp.dibujar_grafica(ele, pr_quw3, "QuickSort-with-3-way-Partitioning")
		gp.dibujar_grafica(ele, pr_dual, "Dual-Pivot-QuickSort")
		gp.dibujar_grafica(ele, pr_tim, "TimSort")
