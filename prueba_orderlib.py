"""
orderlib.py

Autores: Luis Carlos Blanco, 17-10066
         Gabriel Chaurio, 17-10164

Descripcion: Este programa buscara el timepo promedio de ejecucion de los algoritmos 
de ordenamiento implementados en orderlib.py

Ultima modificacion: 17/02/2020
"""
import random
from orderlib import *


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
	if n < 32:
		print('La lista debe tener al menos 32 elementos')
	else: 
		a = ordenado(n)
		print(a)
		for i in range(0,n-8):
			a[i], a[i+8] = a[i+8], a[i]

	return a

def casi_ord_2(n:int) -> list:
	pass

t = int(input('Ingrese el tamano de la lista: '))
z = casi_ord_1(t)
print(z)