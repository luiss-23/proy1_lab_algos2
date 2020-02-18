"""
orderlib,py

Descripcion: Libreria de algoritmos de ordenamiento 

Autores: Luis Carlos Blanco, 17-10066
         Gabriel Chaurio, 17-10126

Ultima modificacion: 18/02/2020
"""
import statistics, math 
#Algoritmo de ordenamiento InsertionSort
#Arreglo a: Arreglo a ordenar
#p,r: casilla inicial y final respectivamente
def insertion_sort_index(a:[int],p,r:int) -> [int]:
	for j in range(p+1, r):
		key = a[j]
		i = j - 1
		while (i >= 0 and a[i] >= key):
			a[i + 1] = a[i]
			i = i - 1
		a[i + 1] = key

	return a

#Algoritmo de ordenamiento Mergesort
#Arreglo t: arreglo a ordenar
def mergesort(t:[int]) -> [int]:

	if len(t) <= 32:
		insertion_sort_index(t,0,len(t))
	else:
		o = len(t) // 2
		p = o + 1
		u = [0] * o
		v = [0] * p

		k = 0
		for i in range(0,o):
			u[i] = t[k]
			k += 1
		for j in range(0,o):
			v[j] = t[j+o]

		mergesort(u)
		mergesort(v)
		merge(u,v,t)

	return t

#Arreglo t: arreglo a ordenar
#Arreglos u,v: arreglos en los que estaran los elementos ordenados para agregar al arreglo t
def merge(u,v,t:[int]) -> [int]:
	m = len(u)
	n = len(v)
	i, j = 0, 0
	u.append(float('inf'))
	v.append(float('inf'))

	for k in range(0, m+n-1):
		if u[i] < v[j]:
			t[k] = u[i]
			i += 1
		else:
			t[k] = v[j]
			j += 1

	return t


#Algoritmo de ordenamiento QuickSort Iterativo
#Arreglo a: arreglo a ordernar
def quicksort_it(a:[int]) -> [int]:
	n, m = 0, 1

	while m < len(a):
		n = n + 1
		m = m * 2

	k, p, q = 0, 0, len(a)
	x = [0 for i in range(0,n)]
	y = [0 for i in range(0,n)]

	while (k != 0 or q - p >= 2):
		if q - p <= 1:
			k = k - 1
			p, q = x[k], y[k]
		elif q - p >= 2:
			z = a[(p+q)//2]
			r, w, b = p, p, q
			while w != b:
				if a[w] < z:
					a[r], a[w] = a[w], a[r]
					r, w = r + 1, w + 1
				elif a[w] == z:
					w = w + 1
				elif a[w] > z:
					b = b - 1
					a[b], a[w] = a[w], a[b] 

			if r - p <= q - w:
				x[k] = w 
				y[k] = q
				q = r
			elif q - w <= r - p:
				x[k] = p
				y[k] = r
				p = w

			k = k + 1

	return a

#Algoritmo de ordenamiento quicksort
#Arreglo a: arreglo a ordenar
#p: casilla inicial del arreglo a
#r: casilla anterior a la final del arreglo a
def quicksort(a:[int],p,r:int) -> [int]:
	if len(a) <= 32:
		insertion_sort_index(a,p,r)
	if p < r:
		q = part(a,p,r)
		quicksort(a,p,q-1)
		quicksort(a,q+1,r)

	return a

#Algoritmo para encontrar el pivote del quicksort
#Arreglo a: arreglo a ordenar 
#p: casilla inicial del arreglo a
#r: casilla anterior a la final del arreglo a
def part(a:[int],p,r:int) -> int:
	x = a[r]
	i = p - 1
	for j in range(p,r):
		if a[j] <= x:
			i += 1
			a[i] , a[j] = a[j] , a[i]
	a[i+1], a[r] = a[r], a[i+1]

	return i + 1

#Algoritmo de ordenamiento median-of-3-quicksort
#Arreglo a: arreglo a ordenar 
#f: casilla inicial del arreglo a
#b: casilla final del arreglo a
def median_of_3_quicksort(a:[int],f,b:int) -> [int]:
	if f - b <= 32:
		insertion_sort_index(a,f,b)

	if f - b > 32:
		quicksort_loop(a,f,b)

	return a

#Algoritmo que ordenara el arreglo a
#Arreglo a: arreglo a ordenar 
#f: casilla inicial del arreglo a
#b: casilla final del arreglo a
def quicksort_loop(a:[int],f,b:int) -> [int]:
	while f - b > 32:
		med = [a[f], a[f+(b-f)//2], a[b-1]]
		mediana = statistics.median(med)
		p = partition(a,f,b,mediana)
		if p - f >= b - p:
			quicksort_loop(a,p,b)
			b = p 
		else:
			quicksort_loop(a,f,p)
			f = p 

	return a

#Algoritmo que realizara la division del arreglo a
#Arreglo a: arreglo a ordenar 
#f: casilla inicial del arreglo a
#b: casilla final del arreglo a
#x: mediana entre el primer, ultimo y elemento del medio 
def partition(a:[int],p,r,x) -> int:
	i = p 
	j = r - 1
	
	while True:
		while a[j] > x:
			j = j - 1
		while a[i] < x :
			i = i + 1

		if i < j :
			a[i], a[j] = a[j], a[i]
		if a[i] == x and a[j] == x:
			return j 

#Algoritmo de ordenamiento introsort
#Arreglo a: arreglo a ordenar 
#f: casilla inicial del arreglo a
#b: casilla final del arreglo a
def introsort(a:[int],f,b:int) -> [int]:
	introsort_loop(a,f,b,2*math.log2(b-f))
	insertion_sort_index(a,f,b)

	return a

#Algoritmo usado por introsort para ordenar el arreglo a 
#f: casilla inicial del arreglo a
#b: casilla final del arreglo a
#depth_limit: maximo de recursion usada por el algoritmo
def introsort_loop(a:[int],f,b:int,depth_limit) -> [int]:
	while b - f > 32:
		if depth_limit == 0:
			heapsort(a)
			return 

		m = [a[f], a[f+(b-f)//2], a[b-1]]
		mediana = statistics.median(m)
		depth_limit -= 1 
		p = partition(a,f,b,mediana)
		introsort_loop(a,p,b,depth_limit)
		b = p

	return a

#Algoritmo de ordenamiento heapsort, usado por introsort para ordenar el arreglo a
#a: arreglo a ordenar
def heapsort(a:[int]) -> [int]:
	build_max_heap(a)
	n = len(a)
	for i in range(n-1,0,-1):
		a[i], a[0] = a[0], a[i]
		max_heapify(a,0,i)

	return a

#Algoritmo usado por heapsort para ordenar el arreglo a
#a: arreglo a ordenar 
def build_max_heap(a:[int]) -> [int]:
	n = len(a)
	for i in range(n, -1, -1):
		max_heapify(a,i,n)

	return a

#Algoritmo usado por heapsort para el ordenamiento del arreglo
#i: elemento a cambiar de posicion
#n: tamaño del arreglo
def max_heapify(a:[int],i,n:int) -> [int]:
	l = 2*i + 1
	r = 2*i

	if l < n and a[i] < a[l]:
		largest = l
	else:
		largest = i 

	if r < n and a[largest] < a[r]:
		largest = r

	if largest != i:
		a[i], a[largest] = a[largest], a[i]
		max_heapify(a,largest,n)

	return a

#Algoritmo de ordenamiento para quicksort with 3 way partitioning 
#a: arreglo a ordenar 
#l: casilla inicial del arreglo a ordenar
#r: casilla final del arreglo a ordenar
def quicksort_w_3_way_partitioning(a:[int],l,r:int) -> [int]:

	if r - l <= 32:
		insertion_sort_index(a,l,r)

	i, j, p, q = l-1, r, l-1, r
	v = a[r]

	if r <= l:
		return

	while True:
		i += 1
		while(a[i] < v):
			i += 1

		j -= 1
		while(v < a[j]):
			if (j == l):
				break
			j -= 1

		if (i >= j):
			break

		a[i], a[j] = a[j], a[i]

		if a[i] == v:
			p += 1
			a[p], a[i] = a[i], a[p]
		if v == a[j]:
			q -= 1 
			a[j], a[q]	= a[q], a[j]


	a[i], a[r] = a[r], a[i]
	j = i -1 
	i = i + 1

	for k in range(l,p):
		a[k], a[j] = a[j], a[k]
		j = j - 1

	k = r - 1
	while (k > q):
		a[i], a[k] = a[k], a[i]
		k -= 1
		i += 1

	quicksort_w_3_way_partitioning(a,l,j)
	quicksort_w_3_way_partitioning(a,i,r)

	return a

#Algoritmo de ordenamiento Dual pivot quicksort
#a: arreglo a ordenar 
#l: casilla inicial del arreglo a ordenar
#r: casilla final del arreglo a ordenar
def dual_pivot_quicksort(a:list,left,right:int) -> list:
	if(right-left <= 32):
		insertion_sort_index(a,left,right+1)
	else:
		if(a[left] > a[right]):
			p , q = a[right] , a[left]
		else:
			p , q = a[left] , a[right]
		l = left + 1
		g = right - 1
		k = l
		while(k <= g):
			if(a[k] < p):
				a[k] , a[l] = a[l] , a[k]
				l += 1
			else:
				if(a[k] >= q):
					while(a[g] > q and k < g):
						g -= 1
					if(a[g] >= p):
						a[k] , a[g] = a[g] , a[k]
					else:
						a[k] , a[g] = a[g] , a[k]
						a[k] , a[l] = a[l] , a[k]
						l += 1
					g -= 1
			k += 1
		l -= 1
		g += 1
		a[left] = a[l]
		a[l] = p
		a[right] = a[g]
		a[g] = q
		dual_pivot_quicksort(a,left,l-1)
		dual_pivot_quicksort(a,l+1,g-1)
		dual_pivot_quicksort(a,g+1,right)

	return a

#Algoritmo de ordenamiento TimSort
#a: arreglo a ordenar
def timsort(a:list) -> list:
	minrun = 32

	n = len(a)

	for i in range(0,n,minrun):
		end = min(i+minrun-1,n-1)
		a = InsSort(a,i,end)

	curr_size = minrun
	while(curr_size < n):    
		for i in range(0,n,curr_size*2):
			mid = min(n-1,i+curr_size-1)
			end = min(n-1,mid+curr_size)
			a = merge_it(a,i,mid,end)
		curr_size *= 2

	return a
	
#Algoritmo de ordenaiento InsertionSort usado pot TimSort
#a: arreglo a ordenar 
#start: casilla inicial del arreglo
#end: casilla final del arreglo
def InsSort(a,start,end):    
    for i in range(start+1,end+1):
        elem = a[i]
        j = i-1
        while j>=start and elem<a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = elem

    return a

#Algoritmo merge usado en timsort
#start: casilla inicial del arreglo
#mid: casilla encontrada en la mitad del arreglo
#end: casilla final del arreglo
def merge_it(a:list,start,mid,end:int) -> list:

    if(mid == end):
        return a

    first = a[start:mid+1]
    last = a[mid+1:end+1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind  = start
     
    while(ind1 < len1 and ind2 < len2):
        if(first[ind1] < last[ind2]):
            a[ind] = first[ind1]
            ind1 += 1
        else:
            a[ind] = last[ind2]
            ind2 += 1
        ind += 1
     
    while(ind1 < len1):
        a[ind] = first[ind1]
        ind1 += 1
        ind += 1
              
    while(ind2 < len2):
        a[ind] = last[ind2]
        ind2 += 1
        ind += 1   
              
    return a