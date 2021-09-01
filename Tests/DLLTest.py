import unittest
from Classes.DoublyLinkedList import DoublyLinkedList as DLL


# MAIN DIFF BETWEEN BINARY AND DOUBLY LINKED:
# BINARY IS ONE MASSIVE INTERCONNECTED OBJECT
# DOUBLYLINKED LIST IS A LIST OF OBJECTS WHERE EACH OBJECT HAS A REFERENCE TO THE NEXT OBJECT

class DLLTest(unittest.TestCase):
    # unittest setup ran to initialise DoublyLinkedList class as an object through alias

    def setUp(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

        # numOfCards = 52  # UNUSED

        self.dll = DLL()

        for suit in suits:
            for value in values:
                self.dll.append(f"{value}-{suit}")

    def tearDown(self):
        pass

    # Test last element added if its the appended value
    def test_append(self):
        self.dll.append("Ace-Spades")
        self.assertEqual(self.dll.tail.data, "Ace-Spades")

    # find given value
    def test_find(self):
        self.assertEqual((self.dll.find_card("Q-Spades")), "Q-Spades")

    # delete given value
    def test_delete(self):
        self.dll.delete_card("Q-Spades")
        self.assertFalse((self.dll.find_card("Q-Spades")), False)

    # cant think of a good test case here because it shows output to console
    def test_revPrint(self):
        self.dll.reverse_print()


if __name__ == '__main__':
    unittest.main()
