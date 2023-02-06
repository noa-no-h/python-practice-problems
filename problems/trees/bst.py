class Empty:

    def __init__(self):
        self.value = None

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())

    def __str__(self):
        return 'empty'
    
    def inorder(self):
        return

    def add_to_all(self):
        #print(self.value)
        return []


class Node:

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
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self):
        print(self.value)
        in_order_list = []
        if self.is_empty():
            return in_order_list
        if not self.left.is_empty():
            in_order_list += self.left.inorder()
        in_order_list += [self.value]
        if not self.right.is_empty():
            in_order_list += self.right.inorder()
        return in_order_list
    
    def min_item(self):
        if self.left.is_empty():
            return self.value
        else:
            return self.left.min_item()

    def __str__(self):
        lines = []
        if self.right:
            found = False
            for line in str(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.value))
        if self.left:
            found = False
            for line in str(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)

    def balance_factor(self):
        return self.right.height() - self.left.height()

    def balanced(self):
        return self.balance_factor() == 0

    def balanced_everywhere(self):
        if not self.balanced():
            return False
        if self.is_leaf():
            return True
        else:
            return self.right.balanced_everywhere() and self.left.balanced_everywhere()

    def add_to_all(self):
        #print(self.value)
        if self.is_empty():
            return
        new_tree = Node(self.value + 1, self.left.add_to_all(), self.right.add_to_all())
        return new_tree

    def path_to(self, n):
        if type(self) is Empty:
            return [self.value]
        else:
            path_list = []
            path_list.append(self.value)
            if n > self.value:
                path_list += self.right.path_to(n)
                return path_list
            if n < self.value:
                path_list += self.left.path_to(n)
                return path_list

            


if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)
    #bst = Empty().insert(42).insert(10).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(str(bst))
    print(f"The min is {bst.min_item()}")
    #print(f"{str(bst.add_to_all())}")
    #print(f"{bst.path_to(15)}")

    print(f'the inorder traversal is {bst.inorder()}')
