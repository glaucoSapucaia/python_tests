def _bacon(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'bacon'
    
    if n % 3 == 0:
        return 'ba'

    if n % 5 == 0:
        return 'con'

    return 'fome'