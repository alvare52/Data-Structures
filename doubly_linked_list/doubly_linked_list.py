"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        # create a new node
        new_node = ListNode(value, None, None)
        self.length += 1
    
        # check to see if DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
    
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # wrap value given in a ListNode
        new_node = ListNode(value, None, None)
        self.length += 1
        # check if there is no head and no tail (empty DLL)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # non empty DLL
        else:
            # make old tail the new tail's prev
            new_node.prev = self.tail
            # make old tail's next = to our new tail node
            self.tail.next = new_node
            # make old tail = to our new tail last
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # grab tail's value
        value = self.tail.value
        # delete the tail, and - 1
        self.delete(self.tail)
        # return value we just deleted, so it's like pop
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # check if the node is the head
        if node is self.head:
            return None
        # store reference to the node we're going to move
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        # add_to_head has a += 1 in it
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return None
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return None
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # check if node is the head
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        # otherwise, there's no addititional steps
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):

        # max = None
        # temp = None

        # temp = max = self.head

        # while temp is not None:
        #     if temp.value > max.value:
        #         max = temp
        #     temp = temp.next
        # return max.value
        # # init a variable that will keep track of the largest element we've seen so far
        current_max = self.head.value
        current = self.head.next
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            current = current.next
        return current_max
