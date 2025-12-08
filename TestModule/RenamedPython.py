def TestFunciton():

    """
    Test auto update.
    
    """
    print('Hello World!')

def TestAdd(a :int, b:int):
    """
    Docstring for TestAdd
    
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    
    :returns: Added Value.
    :rtype: int
    """
    c = a + b
    return c


def TestSubtract(a:int, b:int):
    """
    Docstring for TestSubtract
    
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int

    :returns: Subtracted Value.
    :rtype: int
    """
    c = a - b
    return c


def GenerateSomeTextFromString(input :  str):
	"""
	Something something
	"""
	return "{} with some format".format(str)


def PythonIsInteresting(input : str):
    """

    Python has many functions

    This functions returns True if string size larger than 10.
    """
    value = True if len(input) > 10 else False
    return value


def PrintListFromi(i: int):
    """

    Python has many functions

    This functions returns prints from 0 to i.

    :param i: Description
    :type i: int

    :returns: list all int
    :rtype: list[int]
    """
    return [ j for j in range(i) ]


def NothingIsReal(i: int):
    """

    Python random stuff
    :param i: asuodjfaskdfasfa

    :returns: i squared
    :rtype: int
    """

    return i*i