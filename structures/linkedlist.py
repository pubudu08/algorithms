class Node(object):
    def __init__(self, data):
        """
        The constructor for the linkedlist
        :param data:
        :return:
        """
        self.data = data
        self.next_node = None  # creating a root node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_start(self, data):
        """
         inserting a node at start
         complexity is O(1)
        :param data:
        :return:
        """
        self.size = + self.size
        new_node = Node(data)

        if not self.head:  # first node
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove(self, data):
        if self.head is None:
            return
        self.size -= 1
        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

    def _size(self):
        """
        complexity is O(1)
        :return:
        """
        return self.size

    def __size(self):
        """
        Complexity is O(N)
        :return:
        """
        actual_node = self.head
        size = 0

        while actual_node is not None:
            size += 1
            actual_node = actual_node.next_node
        return size

    def insert_at_end(self, data):
        """
        complexity is O(N)
        inserting at the end is not efficient
        :param data:
        :return:
        """
        self.size += 1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def traverse_list(self):
        actual_node = self.head
        output = "["

        while actual_node is not None:
            output = output + str(actual_node.data) + "]->["
            actual_node = actual_node.next_node
        return output + "None]"

    def reverse_list(self):
        current_node = self.head
        result_node = None

        while current_node is not None:
            next_node = current_node.next_node  # tricky: note the next node
            # move the current node in to the result node
            current_node.next_node = result_node
            result_node = current_node

            # Process the next node
            current_node = next_node
        self.head = result_node

    def merge_list(self, head_node_one, head_node_two):
        if head_node_one is None:
            return head_node_two
        if head_node_two is None:
            return head_node_one

        # create dummy node to avoid additional checks in loop
        s = t = Node(0)
        while not (head_node_one is None and head_node_two is None):
            if head_node_one.data < head_node_two.data:
                # remember current low-node
                current_low = head_node_one
                # follow ->next
                head_node_one = head_node_one.next_node
            else:
                current_low = head_node_two
                head_node_two = head_node_two.next_node
            # only mutate the node AFTER we have followed ->next
            t.next_node = current_low
            # and make sure we also advance the temp
            t = t.next_node
        t.next_node = head_node_one or head_node_two
        # return tail of dummy node
        return s.next_node





linkedlist = LinkedList()
linkedlist.insert_at_start(12)
linkedlist.insert_at_start(23)
linkedlist.insert_at_start(34)


linkedlist2 = LinkedList()
linkedlist.insert_at_start(56)
linkedlist.insert_at_start(57)
linkedlist.insert_at_start(79)

# print(linkedlist.traverse_list())
# linkedlist.insert_at_end(45)
# #
# print(linkedlist.traverse_list())
# linkedlist.remove(34)
# print(linkedlist.traverse_list())
# linkedlist.remove(23)
# print(linkedlist.traverse_list())

# linkedlist.reverse_list()
# print(linkedlist.traverse_list())

print("LinkedList One: " + str(linkedlist.traverse_list()))
print("LinkedList Two: " + str(linkedlist2.traverse_list()))

linkedlist.merge_list(linkedlist.head, linkedlist2.head)
print("Merged in to LinkedList one")

print("LinkedList One: " + str(linkedlist.traverse_list()))
print("LinkedList Two: " + str(linkedlist2.traverse_list()))