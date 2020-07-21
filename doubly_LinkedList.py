class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def add_val(self,*args):
        for value in args:
            if not isinstance(value,Node):
                value = Node (value)
            if self.head == None:
                self.head = value
            else:
                pos = self.head
                while pos.next is not None:
                    pos = pos.next
                prev = pos
                pos.next = value
                pos.next.prev = prev

    def add_val_by_position(self,value,pos):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head == None:
            self.head = value
        else:
            if pos == 1:
                present_head = self.head
                self.head = value
                self.head.next = present_head
                self.head.next.prev = self.head
            else:
                initial_pos = self.head
                for i in range(pos-2):
                    initial_pos = initial_pos.next
                prev = initial_pos
                right_side_nodes = initial_pos.next
                initial_pos.next = value
                initial_pos.next.prev = prev
                initial_pos.next.next = right_side_nodes
                initial_pos.next.next.prev = initial_pos.next


    #Code below shows the pros of doublyLinkedList over singlyLinkedList
    def pop(self):
        pos = self.head
        while pos.next is not None:
            pos = pos.next
        curr = pos
        prev = curr.prev
        prev.next = None

    def del_by_val(self,val):
        pos = self.head
        while pos.data != val:
            pos = pos.next
        prev = pos.prev
        if prev is not None:
            prev.next = pos.next
            pos.next.prev = prev
        else:
            self.head = pos.next
            self.head.prev = prev

    def reverse(self):
        try:
            initial_pos = self.head
            while initial_pos is not None:
                prev = initial_pos.prev
                initial_pos.prev = initial_pos.next
                initial_pos.next = prev
                initial_pos = initial_pos.prev
            if prev is not None:
                self.head = prev.prev
        except UnboundLocalError:
            pass


    def __str__(self):
        try:
            pos = self.head
            entire_linked_list = ""
            while pos.next is not None:
                entire_linked_list += str(pos) + "<->"
                pos = pos.next
            entire_linked_list += str(pos)
            return entire_linked_list
        except AttributeError:
            return "LINKED LIST IS EMPTY"


A= doublyLinkedList()
A.add_val(10)
print(A)
A.add_val(20,40,60,80)
print(A)
A.add_val_by_position(1,4)
print(A)
A.add_val(30)
print(A)
A.pop()
print(A)
A.del_by_val(10)
print(A)
A.del_by_val(40)
print(A)
A.reverse()
print(A)
A.add_val(20,30,40)
print(A)
A.reverse()
print(A)
A.add_val(20,30,40)
print(A)
A.reverse()
print(A)
