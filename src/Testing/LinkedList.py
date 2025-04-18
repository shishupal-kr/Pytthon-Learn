class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
              print(temp.data , end=" -> ")
              temp = temp.next
        print("None")

ll = LinkedList()

ll.insert_first(4)
ll.insert_first(3)
ll.insert_first(2)
ll.insert_first(1)

ll.print_list()