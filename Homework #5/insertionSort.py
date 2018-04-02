'''
    Description:  Sorts myList in ascending order using an insertion sort.
    File:  insertionSort.py
    Author: Mark Fienup
'''

import random
import time

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

def improvedInsertionSort(myList):
    """Rearranges the items in myList so they are in ascending order"""
    for lastUnsortedIndex in range(len(myList) - 1, -1, -1):
        # starts the sort by finding and swapping the largest item with the right-most item
        maxNum = 0
        maxIndex = 0
        for swapIndex in range(0, lastUnsortedIndex):
            if myList[swapIndex] > maxNum: # records highest number seen
                maxNum = myList[swapIndex]
                maxIndex = swapIndex
        # swaps the
        temp = myList[lastUnsortedIndex]
        myList[lastUnsortedIndex] = maxNum
        myList[maxIndex] = temp
        itemToInsert = myList[lastUnsortedIndex]
        # scans from left to right to determine where the right-most unsorted item goes
        testIndex = lastUnsortedIndex + 1
        while testIndex <= len(myList) - 1 and myList[testIndex] < itemToInsert:
            myList[testIndex - 1] = myList[testIndex]
            testIndex += 1

        # Insert the itemToInsert at the correct spot
        myList[testIndex - 1] = itemToInsert

def shuffle(myList):
    for fromIndex in range(len(myList)):
        toIndex = random.randint(0,len(myList)-1)
        temp = myList[fromIndex]
        myList[fromIndex] = myList[toIndex]
        myList[toIndex] = temp


# Time tests
print("---------- DESCENDING ----------")
print("insertionSort Timings")
aList = list(range(10000, 0, -1))
print("Before sorting descending list: ", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print("sorted list:", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
print("Time to sort", end - start, "seconds")
print('')

print("improvedInsertionSort Timings")
aList = list(range(10000, 0, -1))
print("Before sorting descending list: ", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
start = time.clock()
improvedInsertionSort(aList)
end = time.clock()
print("sorted list:", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
print("Time to sort", end - start, "seconds")

print("\n---------- ASCENDING ----------")
print("insertionSort Timings")
aList = list(range(0, 10000))
print("Before sorting descending list: ", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print("sorted list:", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
print("Time to sort", end - start, "seconds\n")

print("improvedInsertionSort Timings")
aList = list(range(0, 10000))
print("Before sorting descending list: ", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
start = time.clock()
improvedInsertionSort(aList)
end = time.clock()
print("sorted list:", end="")
print(aList[0], aList[1], aList[2], '...', aList[-3], aList[-2], aList[-1])
print("Time to sort", end - start, "seconds")

print("\n----------- RANDOM -----------")
print('insertionSort:')
aList = list(range(10000,0,-1))
shuffle(aList)
print( "Before sorting 1st random list: ",end='')
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

aList = list(range(10000,0,-1))
shuffle(aList)
print( "Before sorting 2nd random list: ",end='')
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
insertionSort(aList)
end = time.clock()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

print('\nimprovedInsertionSort:')
aList = list(range(10000,0,-1))
shuffle(aList)
print( "\nBefore sorting 1st random list: ",end='')
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
improvedInsertionSort(aList)
end = time.clock()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

aList = list(range(10000,0,-1))
shuffle(aList)
print( "\nBefore sorting 2nd random list: ",end='')
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.clock()
improvedInsertionSort(aList)
end = time.clock()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")