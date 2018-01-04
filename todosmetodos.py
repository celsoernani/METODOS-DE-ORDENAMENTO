import matplotlib.pyplot as plt
import random
from timeit import timeit
import math
 
listaOrdenadas = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
 
dictListas = {}
bubbleSortList = []
sellectionSortList = []
insertionSortList = []
quickSortList = []
mergeSortList = []
shellSortList = []
countingSortList = []
radixSortList = []
bucketSortList = []
heapSortList = []
 
def criaListaRand(tam):
    newlist = []
    random.seed()
    i=0
    while i<tam:
        num = random.randint(1,10*tam)
        newlist.append(num)
        i+=1
    return newlist
 
def bubbleSort(listToSort):
    for passnum in range(len(listToSort)-1,0,-1):
        for index in range(passnum):
            if listToSort[index]>listToSort[index+1]:
                temp = listToSort[index]
                listToSort[index] = listToSort[index+1]
                listToSort[index+1] = temp
 
def selectionSort(listToSort):
  for position in range(len(listToSort)-1,0,-1):
    maxIndex=0
    for location in range(1,position+1):
      if listToSort[location]>listToSort[maxIndex]:
        maxIndex = location
 
      temp = listToSort[position]
      listToSort[position] = listToSort[maxIndex]
      listToSort[maxIndex] = temp
 
def insertionSort(listToSort):
  for indice in range(1,len(listToSort)):
    valorAtual = listToSort[indice]
    posicao = indice
 
    while posicao>0 and listToSort[posicao-1]>valorAtual:
      listToSort[posicao]=listToSort[posicao-1]
      posicao = posicao-1
 
    listToSort[posicao]=valorAtual
 
def quickSort(listToSort):
   quickSortHelper(listToSort,0,len(listToSort)-1)
 
def quickSortHelper(listToSort,first,last):
   if first<last:
 
       pointOfDivision = partition(listToSort,first,last)
 
       quickSortHelper(listToSort,first,pointOfDivision-1)
       quickSortHelper(listToSort,pointOfDivision+1,last)
 
def partition(listToSort,first,last):
   pivot = listToSort[first]
 
   leftPoint = first+1
   rightPoint = last
 
   done = False
   while not done:
 
       while leftPoint <= rightPoint and listToSort[leftPoint] <= pivot:
           leftPoint = leftPoint + 1
 
       while listToSort[rightPoint] >= pivot and rightPoint >= leftPoint:
           rightPoint = rightPoint -1
 
       if rightPoint < leftPoint:
           done = True
       else:
           temp = listToSort[leftPoint]
           listToSort[leftPoint] = listToSort[rightPoint]
           listToSort[rightPoint] = temp
 
   temp = listToSort[first]
   listToSort[first] = listToSort[rightPoint]
   listToSort[rightPoint] = temp
 
 
   return rightPoint
 
def merge(lefttList,rightList):

    listToReturn = []
    while len(lefttList) != 0 and len(rightList) != 0:
        if lefttList[0] < rightList[0]:
            listToReturn.append(lefttList[0])
            lefttList.remove(lefttList[0])
        else:
            listToReturn.append(rightList[0])
            rightList.remove(rightList[0])
    if len(lefttList) == 0:
        listToReturn += rightList
    else:
        listToReturn += lefttList
    return listToReturn

def mergesort(listToSort):

    if len(listToSort) == 0 or len(listToSort) == 1:
        return listToSort
    else:
        middle = int(len(listToSort)/2)
        lefttList = mergesort(listToSort[:middle])
        rightList = mergesort(listToSort[middle:])
        return merge(lefttList,rightList)

def shellSort(listToSort):
    sublistcount = len(listToSort)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(listToSort,startposition,sublistcount)

      sublistcount = sublistcount // 2

def gapInsertionSort(listToSort,start,gap):
    for index in range(start+gap,len(listToSort),gap):

        currentvalue = listToSort[index]
        position = index

        while position>=gap and listToSort[position-gap]>currentvalue:
            listToSort[position]=listToSort[position-gap]
            position = position-gap

        listToSort[position]=currentvalue

def countingSort(listToSort):
    maximum = max(listToSort)
    minimum = min(listToSort)
    counting_alist = [0]*(maximum-minimum+1)
 
    for i in listToSort:
        counting_alist[i-minimum] += 1
 
    sorted_alist = []
    for i in range(minimum, maximum+1):
        if counting_alist[i-minimum] > 0:
            for j in range(0, counting_alist[i-minimum]):
                sorted_alist.append(i)
 
    return sorted_alist

def radixSort(listToSort):
  RADIX = 10
  isMaxLength = False
  temporary = -1
  local = 1

  while not isMaxLength:
    isMaxLength = True

    buckets = [list() for _ in range(RADIX)]

    for  element in listToSort:
      temporary = element / local
      buckets[math.floor(temporary % RADIX)].append(element)
      if isMaxLength and temporary > 0:
        isMaxLength = False

    index = 0

    for bucketIndex in range(RADIX):
      newBuckets = buckets[bucketIndex]
      for element in newBuckets:
        listToSort[index] = element
        index += 1

    local *= RADIX

def bucketSort(listToSort):
  bucketSize = 3
  if len(listToSort) == 0:
    return listToSort

  minimum = listToSort[0]
  maximum = listToSort[0]
  for i in range(1, len(listToSort)):
    if listToSort[i] < minimum:
      minimum = listToSort[i]
    elif listToSort[i] > maximum:
      maximum = listToSort[i]

  bucketCount = math.floor((maximum - minimum) / bucketSize) + 1
  buckets = []
  for i in range(0, bucketCount):
    buckets.append([])

  for i in range(0, len(listToSort)):
    buckets[math.floor((listToSort[i] - minimum) / bucketSize)].append(listToSort[i])

  listToSort = []
  for i in range(0, len(buckets)):
    insertionSort(buckets[i])
    for j in range(0, len(buckets[i])):
      listToSort.append(buckets[i][j])

  return listToSort

def heapSort( listToSort ):
  length = len( listToSort ) - 1
  leftParent = length / 2
  for index in range ( int(leftParent), -1, -1 ):
    moveDown( listToSort, index, length )
 
  for index in range ( length, 0, -1 ):
    if listToSort[0] > listToSort[index]:
      swap( listToSort, 0, index )
      moveDown( listToSort, 0, index - 1 )
 
 
def moveDown( listToSort, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    if ( largest < last ) and ( listToSort[largest] < listToSort[largest + 1] ):
      largest += 1
 
    if listToSort[largest] > listToSort[first]:
      swap( listToSort, largest, first )
      first = largest;
      largest = 2 * first + 1
    else:
      return
 
def swap( listToSwap, index1, index2 ):
  tmp = listToSwap[index1]
  listToSwap[index1] = listToSwap[index2]
  listToSwap[index2] = tmp


for tamanho in listaOrdenadas:
    dictListas[tamanho] = criaListaRand(tamanho)
    bubbleSortList.append(timeit("bubbleSort({})".format(dictListas[tamanho]),setup="from _main_ import bubbleSort", number=1))
    sellectionSortList.append(timeit("selectionSort({})".format(dictListas[tamanho]),setup="from _main_ import selectionSort", number=1))
    insertionSortList.append(timeit("insertionSort({})".format(dictListas[tamanho]),setup="from _main_ import insertionSort", number=1))
    quickSortList.append(timeit("quickSort({})".format(dictListas[tamanho]),setup="from _main_ import quickSort", number=1))
    mergeSortList.append(timeit("mergesort({})".format(dictListas[tamanho]),setup="from _main_ import mergesort", number=1))
    shellSortList.append(timeit("shellSort({})".format(dictListas[tamanho]),setup="from _main_ import shellSort", number=1))
    countingSortList.append(timeit("countingSort({})".format(dictListas[tamanho]),setup="from _main_ import countingSort", number=1))
    radixSortList.append(timeit("radixSort({})".format(dictListas[tamanho]),setup="from _main_ import radixSort", number=1))
    bucketSortList.append(timeit("bucketSort({})".format(dictListas[tamanho]),setup="from _main_ import bucketSort", number=1))
    heapSortList.append(timeit("heapSort({})".format(dictListas[tamanho]),setup="from _main_ import heapSort", number=1))

fig, ax = plt.subplots()
ax.semilogx(listaOrdenadas, bubbleSortList, label="Bubble Sort")
ax.semilogx(listaOrdenadas, sellectionSortList, label="Selection Sort")
ax.semilogx(listaOrdenadas, insertionSortList, label="Insertion Sort")
ax.semilogx(listaOrdenadas, quickSortList, label="Quick Sort")
ax.semilogx(listaOrdenadas, mergeSortList, label="Merge Sort")
ax.semilogx(listaOrdenadas, shellSortList, label="Shell Sort")
ax.semilogx(listaOrdenadas, countingSortList, label="Counting Sort")
ax.semilogx(listaOrdenadas, radixSortList, label="Radix Sort")
ax.semilogx(listaOrdenadas, bucketSortList, label="Bucket Sort")
ax.semilogx(listaOrdenadas, heapSortList, label="Heap Sort")
 
plt.ylabel("TEMPO")
plt.xlabel("TAMANHO")
  
legend = ax.legend(loc='upper left', shadow=True)
  
frame = legend.get_frame()
frame.set_facecolor('0.90')
  
for label in legend.get_texts():
    label.set_fontsize('large')
  
for label in legend.get_lines():
    label.set_linewidth(1.5)
plt.show()
