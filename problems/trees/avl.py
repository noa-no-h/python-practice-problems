class AVLEmpty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0
    
    def balance_factor(self):
        return None

    def left_heavy(self):
        return False
    
    def right_heavy(self):
        return False

    def rot_left(self):
        return self
    
    def rot_right(self):
        return self
        
    def contains(self, n):
        return False

    def insert(self, n):
        return AVLNode(n, AVLEmpty(), AVLEmpty())
    
class AVLNode:

    def __init__(self, n, left=None, right=None):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return True

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty

    def num_nodes(self):
        return 1+ self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1+ self.left.height() + self.right.height()

    def balance_factor(self):
        return self.right.height() - self.left.height()
    
    def left_heavy(self):
        return self.balance_factor() < 0
    
    def right_heavy(self):
        return self.balance_factor() > 0
    
    def rot_right(self):
        l = self.left
        r = self.right
        ll = l.left
        lr = l.right
        new_right = AVLNode(self.value, lr, r)
        return AVLNode(l.value, ll, new_right)
    
    def rot_left(self):
        l = self.left
        r = self.right
        rl = r.left
        rr = r.right
        new_left = AVLNode(self.value, l, rl)
        return AVLNode(r.value, new_left, rr)

    def contains(self, n):
        if self.value == n:
            return True
        if self.is_empty():
            return False
        else:
            if n > self.value:
                return self.left.contains(n)
            else:
                return self.right.contains(n)

    def insert(self,n):
        if n<self.value:
            new_node = AVLNode(self.value, self.left.insert(n), self.right)
        elif n>self.value:
            new_node = AVLNode(self.value, self.left, self.right.insert(n))
        else:
            return self
        
        if new_node.left_heavy():
            if new_node.left.left_heavy():
                return new_node.rot_right()
            else:
                first_rotation_AVL = AVLNode(new_node.left.rot_right())
                return new_node.rot_right
       
class AVLNode:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + self.left.height() + self.right.height()

    def balance_factor(self):
        return self.right.height() - self.left.height()
    
    def left_heavy(self):
        return self.balance_factor() < 0
    
    def right_heavy(self):
        return self.balance_factor() > 0
    
    def rot_right(self):
        l = self.left
        r = self.right
        ll = l.left
        lr = l.right
        new_right = AVLNode(self.value, lr, r)
        return AVLNode(l.value, ll, new_right)
    
    def rot_left(self):
        l = self.left
        r = self.right
        rl = r.left
        rr = r.right
        new_left = AVLNode(self.value, l, rl)
        return AVLNode(r.value, new_left, rr)

    def contains(self, n):
        if self.value == n:
            return True
        if self.is_empty():
            return False
        elif n > self.value:
            return self.right.contains(n)
        else:
            return self.left.contains(n)

    def insert(self,n):
        if n<self.value:
            new_node = AVLNode(self.value, self.left.insert(n), self.right)
        elif n>self.value:
            new_node = AVLNode(self.value, self.left, self.right.insert(n))
        else:
            return self

        if new_node.left_heavy():
            if new_node.left.left_heavy():
                self.rot_left()
            else:
