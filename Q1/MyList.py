import math
from Teacher import *
from Node import *


class MyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end=" ")
            pt = pt.next
        print("")

    def clear(self):
        self.head = None

    # Q1-1
    def addLast(self, name="", salary=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if not name.startswith("H") and salary < 50:
            new_node = Node((name, salary))
            if not self.head:
                self.head = new_node
            elif self.tail:
                self.tail.next = new_node
                self.tail = new_node
            else:
                self.head.next = new_node
                self.tail = new_node
        pass

    # end def
    # Q1-2
    def f2(self, Z):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        new_node = Node((Z.Name, Z.Salary))
        pt = self.head
        while pt:
            if self.isPrime(pt.next.data[1]):
                new_node.next = pt.next
                pt.next = new_node
                break
            pt = pt.next

        pass

    def isPrime(self, n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    # end def
    # Q1-3
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        prev = None
        temp = self.head
        if temp is not None:
            if self.isPrime(temp.data[1]):
                self.head = temp.next
                temp = None
                return
        while temp:
            if self.isPrime(temp.data[1]):
                break
            prev = temp
            temp = temp.next
        pass
        # end def
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    # Q1-4
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========
        even_head = Node(0)
        odd_head = Node(0)
        self.splitList(even_head, odd_head)
        even_head = even_head.next
        odd_head = odd_head.next
        self.sortList(even_head)
        self.head = self.merge(even_head, odd_head)
        pass

    def splitList(self, even_head, odd_head):
        even = even_head
        odd = odd_head
        curr = self.head
        while curr is not None:
            even.next = curr
            even = even.next
            curr = curr.next
            if curr is not None:
                odd.next = curr
                odd = odd.next
                curr = curr.next
        even.next = None
        odd.next = None

    def sortList(self, node):

        if node is None:
            return
        temp = node
        while temp is not None:
            i = temp.next
            while i is not None:
                if temp.data[1] > i.data[1]:
                    n = i.data
                    i.data = temp.data
                    temp.data = n
                i = i.next
            temp = temp.next

    def merge(self, p, q):
        head = p
        p_curr = p
        q_curr = q

        # swap their positions until one finishes off
        while p_curr != None and q_curr != None:
            # Save next pointers
            p_next = p_curr.next
            q_next = q_curr.next

            # make q_curr as next of p_curr
            q_curr.next = p_next  # change next pointer of q_curr
            p_curr.next = q_curr  # change next pointer of p_curr

            # update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr
        return head



    # end def
