from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if current is none
        if not self.current:
            # Assign current value as the head, even if it's NONE
            self.current = self.storage.head
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

        else:
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.current.next
            elif self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head
            else:
                self.current.insert_before(item)
                next_node = self.current.next
                self.storage.delete(self.current)
                self.current = next_node
                self.storage.length += 1

    def get(self):
        list_buffer_contents = []

        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


b = RingBuffer(3)
b.append('a')
b.append('b')
b.append('c')
b.append('e')
b.append('989')

print(b.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
