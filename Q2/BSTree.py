import math
from Teacher import *
from Node import *
from MyQueue import *


class BSTree:
    def __init__(self):
        self.root = None
        # self.flag = True

    # end def
    def clear(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    # end def
    def visit(self, p):
        if p is None:
            return
        print(f"{p.data}", end=" ")

    # end def
    def preOrder(self, p):
        if p == None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)

    # end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
        # end def

    def postOrder(self, p):
        if p is None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)

    # end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")

    # end def
    def inOrder(self, p):
        if p == None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)
        # end def

    def inVisit(self):
        self.inOrder(self.root)
        print("")

    # end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left is not None:
                my.EnQueue(p.left)
            if p.right is not None:
                my.EnQueue(p.right)
        print("")
        # end def

    def insert(self, name, salary=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if self.root is None:  # root is an attribute, not a variable
            self.root = Node((name, salary))  # Assign!
            return  # Don't continue

        current = self.root
        while True:
            if salary < current.data[1]:
                if not current.left:  # Opposite condition
                    current.left = Node((name, salary))
                    break
                current = current.left
            else:
                if not current.right:  # Opposite condition
                    current.right = Node((name, salary))
                    break
                current = current.right
        pass

    def f2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        self.post_order(self.root)
        pass

    def isComposite(self, n):
        if n <= 3:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return True
                else:
                    return False
    def post_order(self, node):
        if node is None:
            return
        if self.isComposite(node.data[1]):
            self.postOrder(node.left)
            self.postOrder(node.right)
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========

        pass

    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========

        pass

# end class
