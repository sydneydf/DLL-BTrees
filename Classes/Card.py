class Card:
    def __init__(self, data):
        # Card class for DoublyLinkedList with default values set to None for adjacent references so we can save time
        # with head and tails
        self.prev = None
        self.data = data
        self.next = None
