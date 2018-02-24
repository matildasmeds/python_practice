# Tiny implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    # Some way to look at the result.
    # Could look into plotting libraries...
    def print_tree(self):
        child_str = ""
        child_str += str(self.value)
        child_str += ": ("
        if len(self.children) is 0:
            child_str += ")"
            print(child_str)
            return None
        for child in self.children:
            child_str += str(child.value)
            child_str += ","
        child_str = child_str[:-1]
        child_str += ")"
        print(child_str)
        for child in self.children:
            child.print_tree()

class NilNode(Node):
     def __init__(self):
         self.value = None

     def add_child(self, node):
         return None

     def print_tree(self):
         return None

# A nicer way to build this tree?
# Other kind of a tree?
def build_tree():
     n1 = Node(1)
     n3 = Node(3)
     n9 = Node(9)
     n10 = Node(10)
     n15 = Node(15)
     n17 = Node(17)
     n22 = Node(22)
     n30 = Node(30)
     n15.add_child(n10)
     n15.add_child(n22)
     n10.add_child(n3)
     n10.add_child(n9)
     n3.add_child(n1)
     n22.add_child(n17)
     n22.add_child(n30)
     return n15

n = build_tree()
n.print_tree()

# Preorder Traversal: Root, Left, Right
def preorder_traversal(node):
    print(node.value)
    for child in node.children:
        preorder_traversal(child)

print("Preorder Traversal: Root, Left, Right: ")
preorder_traversal(n)

# Postorder Traversal: Left, Right, Root
def postorder_traversal(node):
    for child in node.children:
        postorder_traversal(child)
    print(node.value)

print("Postorder Traversal: Left, Right, Root")
postorder_traversal(n)

# Inorder Traversal: Left, Root, Right
def inorder_traversal(node):
    if node is None: return
    if len(node.children) is 0:
        print(node.value)
        return
    inorder_traversal(node.children[0])
    print(node.value)
    if len(node.children) > 1:
        inorder_traversal(node.children[1])

print("Inorder Traversal: Left, Root, Right")
inorder_traversal(n)

# The following doesn't work !
class Node:
    # The list value is shared with all instances.
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
    #
    def add_child(self, node):
        self.children.append(node)

