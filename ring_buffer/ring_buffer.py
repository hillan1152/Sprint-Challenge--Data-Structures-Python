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
        # if list is empty, add it to the head
        if len(self.storage) is None:
            # add to head
            self.storage.add_to_tail(item)
            # make it the current item
            self.current == item
            print("current item ---> ", item)
        if len(self.storage) < self.capacity:
            # add to tail
            self.storage.add_to_tail(item)
        # if current = capacity:
        if len(self.storage) == self.capacity:
            del self.storage[self.current]
            item = self.current
            self.current.next == self.current
        #       add to head of

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
r.append('o')
