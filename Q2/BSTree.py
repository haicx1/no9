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

        # Corner cases
        if n <= 1:
            return False
        if n <= 3:
            return False

        # This is checked so that we can skip
        # middle five numbers in below loop
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:

            if n % i == 0 or n % (i + 2) == 0:
                return True
            i = i + 6

        return False

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        if self.isComposite(node.data[1]):
            self.visit(node)

    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
        p = self.search_f3()
        self.delByCopy(p)
        pass

    def search_f3(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and self.isComposite(p.data[1]):
                count += 1
            if count == 1:
                return p
            if p.left is not None:
                my.EnQueue(p.left)
            if p.right is not None:
                my.EnQueue(p.right)
        return None

    def delByCopy(self, p):
        if not p:
            return
        rightmost = p.left
        parent = None
        while rightmost.right:
            parent = rightmost
            rightmost = rightmost.right
        p.data = rightmost.data
        if parent:
            parent.right = rightmost.left
        else:
            p.left = rightmost.left

    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========
        p = self.search_f4()
        self.rotate_left(p)
        pass

    def search_f4(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.right and self.isPrime(p.data[1]):
                count += 1
            if count == 1:
                return p
            if p.left is not None:
                my.EnQueue(p.left)
            if p.right is not None:
                my.EnQueue(p.right)
        return None

    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:  # nếu node con bên trái hoặc bên phải bằng node thì trả về root(root là node cha của node)
            return root
        if node.val < root.val:
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)

    def rotate_left(self, node):
        if not node:  # Kiểm tra nút đầu vào có tồn tại hay không, nếu không thì trả về giá trị None.
            return None
        right_node = node.right  # Lưu lại nút phải của nút đầu vào và nút con trái của nút phải đó
        if not right_node:  # Xử lý trường hợp right_node không tồn tại
            return node
        right_left_node = right_node.left
        node.right = right_left_node  # Xoay trái cây con của node
        right_node.left = node
        if node == self.root:  # Nếu node là nút gốc của cây, nút gốc mới là right_node
            self.root = right_node
        else:  # Nếu node không phải nút gốc, cập nhật con trỏ của nút cha để trỏ đến right_node
            parent = self._find_parent(self.root,
                                       node)  # Cần tìm ra cha của nút được xoay để cập nhật con trỏ của cha đến nút right_node mới sau khi xoay trái
            if parent.left == node:  # Nếu nút được xoay là node con bên trái của nút parent thì cập nhật con trỏ trái của nút parent đến nút right_node
                parent.left = right_node
            else:  # Nếu nút được xoay là node con bên phải của nút parent thì cập nhật con trỏ phải của nút parent đến nút right_node
                parent.right = right_node
        return right_node

    # end class
    def isPrime(self, n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
