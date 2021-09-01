from Classes.Card import Card


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Beginning
        self.tail = None  # End

    def __len__(self):
        pass

    # Data then create Card and append to List
    def append(self, data):
        if self.head is None:
            # create new Card object with parsed data
            self.head = Card(data)
        else:
            # create new Card object with parsed data,
            # this new Card will be APPENDED onto end of list, it is the end of the current list,
            # our changes will need to reflect this!
            new_card = Card(data)
            # set current card equal to the current head of the list
            curr_card = self.head

            '''
            Now this is quite cool
            while the current card.next property is filled
            assign new curr_card
            
            this will stop when curr_card is blank
            '''
            while curr_card.next:
                curr_card = curr_card.next

            # Once curr_card.next is found to be none, assign curr_card.next property equal to the newly created card.
            curr_card.next = self.tail = new_card
            new_card.prev = curr_card
            new_card.next = None

    def prepend(self, data):
        # Didn't need to do this
        if self.head is None:
            self.head = Card(data)
        else:
            new_card = Card(data)
            self.head.prev = new_card
            new_card.next = self.head
            self.head = new_card
            new_card.prev = None

    def find_card(self, card2Find):
        # initialise entry
        curr_card = self.head
        # while loop to process
        while curr_card:
            if curr_card.data == card2Find:
                return curr_card.data
            else:
                # if not curr_card.data then move to next in list
                curr_card = curr_card.next

    def delete_card(self, card2Dlt):
        # initialise entry
        curr_card = self.head
        while curr_card:
            # check if card2dlt found and if its the head
            if curr_card.data == card2Dlt and curr_card == self.head:
                if not curr_card.next:
                    # delete itself plus head reference
                    curr_card = self.head = None
                    return
                else:
                    # temp store next card
                    next = curr_card.next
                    # then delete it and corresponding adjacent references
                    curr_card.next = next.prev = curr_card = None

                    self.head = next
                    return
            elif curr_card.data == card2Dlt:
                if curr_card.next:
                    # Stretch the gap
                    # use temp store to stretch around the old deletion like healing a wound thats deleted
                    # assign references accordingly then delete
                    next = curr_card.next
                    prev = curr_card.prev
                    prev.next = next
                    next.prev = prev
                    curr_card.next = curr_card.prev = curr_card = None
                    return
                else:
                    prev = curr_card.prev
                    prev.next = curr_card.prev = curr_card = None
                    return
            # only used for changing iteration if none of the above conditions are satisfied
            curr_card = curr_card.next

    def reverse_print(self):
        # Get beginning of list as an entry
        curr_card = self.tail

        # iterate through list by printing and then assigning new current card

        while curr_card:
            print(curr_card.data)
            curr_card = curr_card.prev
