"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author: Andrew Walker
"""

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list."""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no previous item.")
        return self._current.getPrevious() != self._header

    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no first item.")
        self._current = self._header.getNext()

    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no last item.")
        self._current = self._trailer.getPrevious()

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item  has moved to the right one item"""
        if not self.hasNext():
            raise AttributeError("The current item does not have a next item.")
        self._current = self._current.getNext()

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one item"""
        if not self.hasPrevious():
            raise AttributeError("The current item does not have a previous item.")
        self._current = self._current.getPrevious()

    def insertAfter(self, item):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self.isEmpty():
            newNode = Node2Way(item)
            newNode.setNext(self._trailer)
            self._trailer.setPrevious(newNode)
            newNode.setPrevious(self._header)
            self._header.setNext(newNode)
            self._size = 1
            self._current = newNode
        else:
            temp = self._current.getNext()
            newNode = Node2Way(item)
            newNode.setNext(temp)
            temp.setPrevious(newNode)
            newNode.setPrevious(self._current)
            self._current.setNext(newNode)
            self._current = newNode
            self._size += 1

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self.isEmpty():
            newNode = Node2Way(item)
            newNode.setNext(self._trailer)
            self._trailer.getPrevious(newNode)
            newNode.setPrevious(self._header)
            self._header.setNext(newNode)
            self._size = 1
            self._current = newNode
        else:
            temp = self._current.getPrevious()
            newNode = Node2Way(item)
            newNode.setNext(self._current)
            self._current.setPrevious(newNode)
            newNode.setPrevious(temp)
            temp.setNext(newNode)
            self._current = newNode
            self._size += 1

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        if self.isEmpty():
            raise AttributeError("You can not request the current item because the list is empty.")
        else:
            return self._current.getData()

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("You can not remove the current item because the list is empty.")
        else:
            if self._current.getNext() == self._trailer:
                self._current.getPrevious().setNext(self._trailer)
                self._trailer.setPrevious(self._current.getPrevious())
                self._current = self._current.getPrevious()
            else:
                tempNext = self._current.getNext()
                tempPrevious = self._current.getPrevious()
                tempNext.setPrevious(tempPrevious)
                tempPrevious.setNext(tempNext)
                self._current = self._current.getNext()


    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("You can not replace the current item because the list is empty.")
        else:
            self._current.setData(newItemValue)

    def isEmpty(self):
        if self._size == 0:
            return True
        return False

    def __len__(self):
        """ Returns the number of items in the list."""
        # replace below
        return self._size

    def __str__(self):
        """Includes items from first through last."""
        resultString = "(head)\n"
        current = self._header.getNext()
        while current.getNext() is not None:
            resultString += " " + str(current.getData())
            current = current.getNext()
        resultString = resultString + "(tail)"
        return resultString

