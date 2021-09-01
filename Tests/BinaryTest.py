import unittest
from Classes.BinarySearch import BinarySearch as BinSearch


class BinaryTest(unittest.TestCase):
    # unittest setup ran to initialise BinarySearch class as an object through alias
    def setUp(self):
        self.binSearch = BinSearch()

    # decode and assert SOS morse to SOS string
    def test_stringDecode(self):
        self.assertEqual(self.binSearch.decodeString('... --- ...'), 'SOS')


if __name__ == '__main__':
    unittest.main()
