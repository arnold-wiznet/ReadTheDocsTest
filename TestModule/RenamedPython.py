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
