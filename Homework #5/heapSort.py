""" Heap Sort
author: Mark Fienup"""
from binheap import BinHeap
# methods: BinHeap(), insert(item), delMin(), isEmpty(), size()

def heapSort(myList):
    # Create an empty heap
    minHeap = BinHeap()

    # Add all list items to minHeap
    for item in myList:
        minHeap.insert(item)

    # delMin heap items back to list in sorted order
    for item in range(len(myList)):
        myList[item] = minHeap.delMin()

def improvedHeapSort(myList):

    # Create empty heap list
    maxHeap = []

    # Add myList items to maxHeap
    for item in myList:
        maxHeap.append(item)

    # Heapify maxHeap
    height = len(maxHeap) // 2
    for item in myList:
