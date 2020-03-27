from doubly_linked_list import DoublyLinkedList
# UNDERSTAND:
#   Has a fixed size = capacity
#       The CAPACITY IS WHAT IS BEING PASSED IN THE RINGBUFFER
#   When capacity is full & add new element, oldest element is overwritten--- LRU CACHE
#   Methods:
#       Append - adds elements to buffer
#       Get - returns ALL elements in the buffer list in their given order
#             should not return NONE


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
    # I CAN USE CURRENT AS A CURSOR OVER THE OLDEST POSSIBLE ITEM, TO REPLACE WHEN IT IS

    def append(self, item):
        if self.storage.length == self.capacity:
            # if nothing is selected as current, make it the head
            if self.current is None:
                # make the head current
                self.storage.head == self.current
            # if the current is the head, delete the value, replace the head, and create next current value
            if self.current.value == self.storage.head.value:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current == self.current.next
            else:
                # delete the current value
                self.storage.delete(self.current)
                # add item to that value
                self.current = item
                self.current.next == self.current
                # make current the next value
                if self.current.next is None:
                    self.current == self.current.head.value
        # if list is empty OR less than capacity, add to tail
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


r = RingBuffer(4)
r.append('a')
r.append('e')
r.append('i')
print(r.append('o'))
