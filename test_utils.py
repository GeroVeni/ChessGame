""" Unit test for functions in utils """
from functools import reduce
from utils import *

def test_makeMoves():
    """ Tests the PGN string splitter """
    
    randList = ["234", "efqwer", "lwjeaf", "+#+#==x", "faskdj", "dxe3=Q"]
    outList = reduce( (lambda x, y: x + y),
        [str(i + 1) + "." + randList[2 * i] +  " " + randList[2 * i + 1] + " " for i in range(len(randList) // 2)])
    assert(makeMoves(outList) == randList)
