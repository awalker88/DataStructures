""" File:  timeHeapSort.py
    Description:  Times the heap sort algorithm on random data
    Author: Mark Fienup"""

import time
import random
from heapSort import heapSort, improvedHeapSort

def main():
    # heapSort
    n = int(input("Enter the number of items you would like to sort: "))
    myList = []
    for index in range(n):
        myList.append(random.randint(1, n))

    #print( "Unsorted List:", myList)
    start = time.clock()

    heapSort(myList)

    endSort = time.clock()

    # print( "Sorted List:  ", myList)
    print("Total improved heap sort time of", n, "random items %5.4f" % (endSort - start))

    # improvedHeapSort

    start = time.clock()

    improvedHeapSort(myList)

    endSort = time.clock()

    print("Total heap sort time of", n, "random items %5.4f" % (endSort - start))

main()
