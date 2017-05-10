class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):
    """
    TODO: Add detailed description about binary search tree operations
    O(logN) time complexity for search, remove and insertion
    It is important to construct a data structure which has a predictable complexity
    Facebook

    Keeps the keys in sorted order so that lookup and other operations can use the principle od binary search

    Every node can have at most two children
    left child smaller than the parent
    right child is greater than the parent

    why is it good? on every decision we get itd of half of the data in which we are searching
    o(logN) time complexity

    height of a tree: the # of layers it contains # of nodes 2^h-1 where h is # of layers
    In general h ~ O(logN) if this is true the tree is said to be balanced if it is not true tree is unbalanced, which
    means asymmetric which is a problem

    We should keep the height of the tree minimum which is h = logN
    if the tree is unbalanced h = logN relation is no more valid and the operation running is no more logarithmic

            Average Case     Worst Case
    Space   O(N)            O(N)
    Insert  O(logN)         O(N)
    Delete  O(logN)         O(N)
    Search  O(logN)         O(N)

    """

    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        We start at the root node, if the data we want to insert is greater than the root node we co th the right, if
        it is smaller we fot he left and so on.
        we discard half of the tree every time

        """
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:  # considering left sub tree
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, root):
        if root.left_child:
            return self.get_min(root.left_child)
        return root.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, root):
        if root.right_child:
            return self.get_max(root.right_child)
        return root.data

    def find(self, data):
        """
            We start at the root node. if the data we want to find is greater than the root node we fo the right, if it
            smaller then we go to the left
            on every decision we discard half of the tree, so it is like binary search in a sorted array O(logN)

            find the smallest node, we just have to go to the left as far as possible, it will be the smallest
            find the largest node, we just have to go to the right as far as possible, it will be the largest

        """

    def remove_node(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print(" removing a leaf node")
                del node
                return None
            if not node.left_child:
                print(" removing a node with single right child node")
                temp_node = node.left_child
                del node
                return temp_node
            elif not node.right_child:
                print(" removing a node with single left child node")
                temp_node = node.right_child
                del node
                return temp_node
            print(" removing node with two children")
            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data,node.left_child)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node

    def remove(self, data):
        """
            soft delete --> we do not remove the node from BST we just mark it has been removed
            complexity: we have to find the item itself + we have to delete it or set it to NULL
            ~ O(logN) find operation + O(1) deletion = O(logN)

            we want to get rid of node that has one child, just we need to update the reference
             complexity: we have to find the item itself + we have to update the reference ( set parent pointer point
             to it's grandchild directly
            ~ O(logN) find operation + O(1) update reference = O(logN)

            we want to get rid of a node that has two children
                we have two options: we look for the largest item in the left subtree (predecessor) OR the smallest item
                 in the right subtree (successor)

                 We look for the predecessor ans swap the two nodes, once you done set the node to null

                We look for the successor ans swap the two nodes, become the case 2, once you done update the
                node references
                Time complexity: O(logN)
        """
        if self.root:
            self.root = self.remove_node(data, self.root)

    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        """
            we visit the left subtree + root + right subtree
            by default it will sort items in numnerically or alphebetically
        """
        # visit left subtree recursively
        if node.left_child:
            self.in_order_traversal(node.left_child)
        print("%s", node.data)  # print the root node
        # right subtree
        if node.right_child:
            self.in_order_traversal(node.right_child)

    def pre_order_traversal(self, node):
        """
            we visit the root  + left + right subtree

        """

    def post_order_traversal(self, node):
        """
            we visit the left subtree + right + root
        """


bst = BinarySearchTree()
bst.insert(12)
bst.insert(5)
bst.insert(7)
bst.insert(657)
bst.insert(234)
bst.insert(1)

print("Min value", bst.get_min_value())
print("Max value", bst.get_max_value())

bst.remove(5)

bst.traverse()
