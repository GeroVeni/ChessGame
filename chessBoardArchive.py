""" Archive storage that enables undo / redo funtionality """

class ChessBoardArchive:
    """ Class that stores and handles changes in board state """

    def __init__(self):
        self.stateList = [None]
        self.pos = 0

    def addState(self, state):
        self.pos += 1
        if (self.pos < len(self.stateList)):
            self.stateList = self.stateList[:self.pos]
        self.stateList.append(state)

    def undo(self):
        if (self.pos > 0):
            self.pos -= 1
        return self.stateList[self.pos]

    def redo(self):
        if (self.pos + 1 < len(self.stateList)):
            self.pos += 1
        return self.stateList[self.pos]
