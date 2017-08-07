""" Unit test for the Color class """

from color import Color


def test_color_constructor():
    """ Tests the creation of new colors """

    col = Color(100, 200, 300)
    assert(col.data == None)

    col = Color(50, 100, 150)
    assert(col.data == (50, 100, 150))
