# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to last node
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
ll = LinkedList()

# Insert elements
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

# Display list
ll.display()