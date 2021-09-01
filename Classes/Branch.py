class Branch:
    def __init__(self, char='', left=None, right=None):
        # Branch class for Binary Search default values assigned in case the actual Branch is instead the end of a
        # sequence and would be called the leaf
        self.char = char
        self.left = left
        self.right = right
