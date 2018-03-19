'''
    Description:  Sorts myList in ascending order using an insertion sort.
    File:  insertionSort.py
'''

def insertionSort(myList):
    """Rearranges the items in myList so they are in ascending order"""
    for firstUnsortedIndex in range(1,len(myList)):
        itemToInsert = myList[firstUnsortedIndex]
        # Scan the sorted part from the right side
        # Shift items to the right while you have not scanned past the left
        # end of the list and you have not found the spot to insert
        testIndex = firstUnsortedIndex - 1
        while testIndex >= 0 and myList[testIndex] > itemToInsert:
            myList[testIndex+1] = myList[testIndex]
            testIndex = testIndex - 1

        # Insert the itemToInsert at the correct spot
        myList[testIndex + 1] = itemToInsert

import random

def shuffle(myList):
    for fromIndex in range(len(myList)):
        toIndex = random.randint(0,len(myList)-1)
        temp = myList[fromIndex]
        myList[fromIndex] = myList[toIndex]
        myList[toIndex] = temp
    

import time

print("insertionSort Timings")            
aList = list(range(10000,0,-1))
print( "\nBefore sorting list: ",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print( "sorted list:", end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

print( "\nBefore sorting list: ", end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print( "sorted list:", end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

aList = list(range(10000,0,-1))
shuffle(aList)
print( "\nBefore sorting (random) list: ",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

aList = list(range(10000,0,-1))
shuffle(aList)
print( "\nBefore sorting (random) list: ",end='')
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

input("Hit <Enter>-key to end")
