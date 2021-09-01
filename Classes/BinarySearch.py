from Classes.Branch import Branch


class BinarySearch:
    def __init__(self):
        # Self.morseList is one HUGE binary Tree ONE OBJECT
        # We traverse the tree by checking each branch and going either left or right during decode
        #
        # Root Branch
        self.morseObject = Branch('',
                                  # LEFTMAINBRANCH
                                  Branch('E',
                                         Branch('I',
                                                Branch('S',
                                                       Branch('H', Branch('5'), Branch('4')),
                                                       Branch('V', Branch(''), Branch('3'))
                                                       ),
                                                Branch('U',
                                                       Branch('F', Branch(''), Branch('')),
                                                       Branch('', Branch(''), Branch('2'))
                                                       )
                                                ),
                                         Branch('A',
                                                Branch('R',
                                                       Branch('L', Branch(''), Branch('')),
                                                       Branch('', Branch('+'), Branch(''))
                                                       ),
                                                Branch('W',
                                                       Branch('P', Branch(''), Branch('')),
                                                       Branch('J', Branch(''), Branch('1'))
                                                       )
                                                )
                                         ),
                                  # RightMainBranch
                                  Branch('T',
                                         Branch('N',
                                                Branch('D',
                                                       Branch('B', Branch('6'), Branch('=')),
                                                       Branch('X', Branch('/'), Branch(''))
                                                       ),
                                                Branch('K',
                                                       Branch('C', Branch(''), Branch('')),
                                                       Branch('Y', Branch(''), Branch(''))
                                                       )
                                                ),
                                         Branch('M',
                                                Branch('G',
                                                       Branch('Z', Branch('7'), Branch('')),
                                                       Branch('Q', Branch(''), Branch(''))
                                                       ),
                                                Branch('O',
                                                       Branch('', Branch('8'), Branch('')),
                                                       Branch('', Branch('9'), Branch('0'))
                                                       )
                                                )
                                         )
                                  )

    def decodeChar(self, sequence):
        # assign INITIAL root of binary tree
        root = self.morseObject
        # for loop to change root depending on left choice for a '.' segment or right choice with an inline variable
        # statement
        for segment in sequence:
            root = root.left if segment == '.' else root.right
        # if above condition NOT met default to returning last value of TREE sequence
        else:
            return root.char

    def decodeString(self, str2Decode):
        # Example str2Decode = '... --- ...'
        endMSG = ''
        # Use Space as the letter seperator and new words represented by a ' / '
        sequencedMorse = str2Decode.split(' ')  # ['...', '---', '...']
        for preChar in sequencedMorse:
            # Check if new word and add space else decode specific segment to a character
            if preChar == '/':
                endMSG += ' '
            else:
                # Once Letter is found add that to endMSG
                endMSG += self.decodeChar(preChar)
        return endMSG
