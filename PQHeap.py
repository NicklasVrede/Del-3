#Navne: 
#Nicklas Enøe Vrede, nickh13
#Mike Brydegaard, mibry23
#Jakob, jamar23


def getMinimum(A):
    if len(A) < 1:
        raise IndexError("Heapunder flow - No elements in list")
    return A[0]

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def extractMin(A):
    if len(A) == 0:
        return None
    min = A[0]
    A[0] = A[len(A)-1] # Assign the value of the last element to the root.
    A.pop() # Remove the last element.
    minHeapify(A, 0) # Reorganize the heap.
    return min

def minHeapify(A, i):
    l = left(i) #venstre indeks
    r = right(i) #højre indeks
    if l < len(A)-1 and A[l] < A[i]: #Test om venstre "findes" og om den er mindre end værdi på i.
        smallest = l #mindste værdis indeks
    else:
        smallest = i

    if r < len(A)-1 and A[r] < A[smallest]: #samme for højre.
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i] #byt rundt.
        minHeapify(A, smallest)

def insert(A:list, e):
    i = len(A) #ikke -1, da vi skal bruge index af et nye sidste element.
    A.append(e)
    while i > 0 and A[parent(i)] > A[i]: #Så længe forældrenoden er større end den nye node.
        A[parent(i)], A[i] = A[i], A[parent(i)] #byt
        i = parent(i) #opdater i indeks til ny plads.

def createEmptyPQ():
    return []





