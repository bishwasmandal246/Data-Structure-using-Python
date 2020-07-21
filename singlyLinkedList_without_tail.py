#All the methods are inplace

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


    def __str__(self):
        return str(self.data)

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def add_val(self,*args):
        for value in args:
            if not isinstance(value,Node):
                value = Node(value)
            if self.head == None:
                self.head = value
            else:
                last = self.head
                while last.next is not None:
                    last = last.next
                last.next = value


    #indexing starts from 1
    def add_val_by_position(self,value,pos):
        if not isinstance(value,Node):
            value = Node(value)
        if self.head == None:
            self.head = value

        else:
            if pos==1:
                right_side_nodes = self.head
                self.head = value
                self.head.next = right_side_nodes
            else:
                initial_pos = self.head
                for i in range (1,pos-1):
                    initial_pos = initial_pos.next
                right_side_nodes = initial_pos.next
                initial_pos.next = value
                initial_pos.next.next = right_side_nodes


    def pop(self):
        try:
            if self.length()<1:
                self.head = None
            else:
                pos = self.head
                while pos.next.next is not None:
                    pos = pos.next
                pos.next = None
        except AttributeError:
            self.head = None



    def del_by_position(self,pos):
        if pos==1:
            self.head = self.head.next
        else:
            initial_pos = self.head
            for i in range(1,pos-1):
                initial_pos = initial_pos.next
            initial_pos.next = initial_pos.next.next

    #Delete the first appearing given value
    def del_by_val(self,val):
        try:
            pos = self.head
            if pos.data == val:
                self.head = pos.next
            else:
                while pos.next.data != val:
                    pos = pos.next
                pos.next = pos.next.next
        except AttributeError:
            print("Value not present in Linked list")


    #deleting all presence of given value
    def del_by_val_all(self,val):
        try:
            print("DEL")
            pos = self.head
            while pos is not None:
                if self.head.data == val:
                    self.head = pos.next
                else:
                    while pos.next.data == val:
                        pos.next = pos.next.next
                pos = pos.next
        except AttributeError:
            pass


    def length(self):
        try:
            ln = 0
            pos = self.head
            while pos.next is not None:
                pos = pos.next
                ln+=1
            ln+=1
            return ln
        except AttributeError:
            return 0


    def count(self,val):
        cnt = 0
        pos = self.head
        while pos is not None:
            if val == pos.data:
                cnt+=1
            pos = pos.next
        return cnt


    def reverse(self):
        if self.length()==0:
            return "No Elements in the linked list"
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


    def __str__(self):
        entire_linked_list=""
        if self.head == None:
            return "Link List is Empty"
        present_pointer = self.head
        while present_pointer.next is not None:
            entire_linked_list+=str(present_pointer.data)+"->"
            present_pointer = present_pointer.next
        entire_linked_list+=str(present_pointer.data)
        return entire_linked_list


if __name__=="__main__":
    A=singlyLinkedList()
    A.add_val(1,2,3,4,5)
    print(A)
    A.add_val_by_position(7,3)
    print(A)
    A.pop()
    print(A)
    A.del_by_position(3)
    print(A)
    A.del_by_val(2)
    print(A)
    A.add_val(7)
    print(A)
    print(A.length())
    A.reverse()
    print(A)
    print("ADDING AGAIN")

    print(A.count(10))
    A.add_val(7)
    print(A)
    A.add_val(7)
    print(A)
    A.add_val(7)
    print(A)
    A.add_val_by_position(7,1)
    print(A)
    A.add_val_by_position(7,1)
    print(A)
    A.del_by_val_all(7)
    print(A)
    A.add_val(100)
    print(A)
    A.pop()
    print(A)
    A.pop()
    print(A)
