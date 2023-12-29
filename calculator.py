def soma(x, y):
    '''Soma x e y
    
    >>> soma(10, 20)
    30

    >>> soma('10', 30)
    Traceback (most recent call last):
    ...
    AssertionError: x deve ser int ou float
    '''
    assert isinstance(x, (int, float)), 'x deve ser int ou float'
    assert isinstance(y, (int, float)), 'y deve ser int ou float'
    return x + y

def subtrai(x, y):
    '''Subtrai x e y

    >>> subtrai(30, 50)
    -21
    '''
    return x - y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)