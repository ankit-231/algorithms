# LinkedList is a datatype like an array that has a head (first element) and tail (last element).
# Each element is called a Node. Each Node contains the information about the next Node, which
# means that if a Node has no info about the next Node, the LinkedList is empty or it is the tail.
# However, we keep track of what head is, so if head has no next Node, LinkedList is empty;
# if another Node has no next Node, it is the tail.
# Singly LinkedList: where each Node has info about only the next Node
# Doubly LinkedList: where each Node has info about both previous and next Node


# Create a Node class
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self):
        self.head: Node = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns number of Nodes in the list
        Takes O(n) time -> since for each added Node, we need to loop that many times
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds the item to the head of the list.
        Takes O(1) time -> constant time as it's just assigning and reassigning variable which
        according to python docs is constant time operation.
        """
        node = Node(data)
        node.next_node = self.head
        self.head = node

    def __repr__(self) -> str:
        """
        Returns a string representaion of the list
        Takes O(n) time
        """
        nodes = []

        current = self.head

        while current:
            if current == self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "-> ".join(nodes)

    def search(self, key):
        """
        Search for the first Node containing data that matches the key
        Return Node or `None` if not found

        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts new Node containing data at any position.
        Insertion takes O(1) time but finding the node at the position
        takes O(n) time.

        Takes overall O(n) time.
        """
        if index == 0:
            self.add(data)
        # To insert at 3rd position
        # [Head: 5]-> [4]-> [3]-> [2]-> [Tail: 1]
        #     0        1     2     3        4
        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            # position = 3   2
            # current = [4]  [3] --> we need this (it is at 2 index)
            # position = 2   1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key.
        Returns Node or None if the key does not exist.
        Takes O(n) time --> Cause in the worst case scenario (i.e key is the last Node, we
        loop through entire LinkedList)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    """
    When you remove a node from the linked list by unlinking it, the memory allocated for that node is still present until the garbage collector in Python reclaims it. However, as long as there are no references to that node, it becomes eligible for garbage collection.

    In Python, memory management is handled by the garbage collector, which automatically reclaims memory occupied by objects that are no longer referenced by any part of the program. When you remove a node from the linked list, you ensure that no part of your linked list has a reference to that node, making it eligible for garbage collection.
    """
