import hug


@hug.type()
def type_enigma_settings(value):
    """The rotors start positions, consists of 3 characters e.g. ('V','B','Q')"""
    alphabetical_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for k in value:
        if k not in alphabetical_chars:
            raise ValueError('Must consist of alphabetical characters only, no punctuation or numbers')
    if len(values) != 3:
        raise ValueError('Must consist of 3 characters')
    return value.upper()


@hug.type()
def type_enigma_rotors(value):
    """The rotors and their order e.g. (2,3,1). There are 8 possible rotors."""
    for k in value:
        if not k.isdigit() or k < 1 or k > 8:
            raise ValueError('Rotor position must be a whole number between 1 and 8')
    return value



@hug.type()
def type_enigma_reflector(value):
    """The reflector in use, a single character 'A','B' or 'C'"""
    if value not in ['A', 'B', 'C', 'a', 'b', 'c']:
        raise ValueError('Reflector must be A, B or C')
    return value.upper()


@hug.type()
def type_enigma_ringstellung(value):
    """The ring settings, consists of 3 characters e.g. ('V','B','Q')"""
    alphabetical_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for k in value:
        if k not in alphabetical_chars:
            raise ValueError('Must consist of alphabetical characters only, no punctuation or numbers')
    return value.upper()


@hug.type()
def type_enigma_steckers(value):
    """The plugboard settings, indicating which characters are replaced by which others. Consists of a 10-tuple of 2-tuples e.g. [('P','O'), ('M','L'), ('I','U'), ('K','J'), ('N','H'), ('Y','T'), ('G','B'), ('V','F'), ('R','E'), ('D','C')]. If fewer plugs are required leave them out e.g. a 5-tuple of 2-tuples would be used if 5 plugs were applied."""
    if len(value) != 10:
        raise ValueError('Must consist of 10-tuple of 2-tuples')
    for k in value:
        if len(k) != 2:
            raise ValueError('Must consist of 10-tuple of 2-tuples')
    return value


@hug.type()
def type_m209_lugpos(value):
    """The lugs, a 27-tuple of 2-tuples"""
    if len(value) != 27:
        raise ValueError('Must consist of 27-tuple of 2-tuples')
    for k in value:
        if len(k) != 2:
            raise ValueError('Must consist of 27-tuple of 2-tuples')
    return value


@hug.type()
def type_m209_wheel_starts(value):
    """The rotor start positions, consists of 6 characters e.g. "AAAAAA". Note that not all character combinations are possible, e.g. wheel 6 has only 17 characters."""
    if len(value) != 6:
        raise ValueError('Must consist of 6 characters')
    return value


class type_m209_wheel(hug.types.length):
    def __init__(self, wheel, size):
        self.wheel = wheel
        self.size = size

    @property
    def __doc__(self):
        return 'Wheel {0} settings, an array of {1} binary values'.format(self.wheel, self.size)

    def __call__(self, value):
        l = len(value)
        if length < self.size:
            raise ValueError("'{0}' is shorter than {1}".format(value, self.size))
        if length >= self.size:
            raise ValueError("'{0}' is longer than {1}".format(value, self.size))
        for k in value:
            if k not in [1,0,'1','0']:
                raise ValueError('Must be a binary value (1|0)')
        return value




@hug.type()
def type_alphabetical_key(value):
    """The keyword, any word or phrase will do. Must consist of alphabetical characters only, no punctuation or numbers"""
    alphabetical_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for k in value:
        if k not in alphabetical_chars:
            raise ValueError('Must consist of alphabetical characters only, no punctuation or numbers')
    return value


@hug.type()
def type_key_alphabet_permutation(value):
    """The key, a permutation of the 26 characters of the alphabet"""
    if len(value) != 26:
        raise ValueError('Must be a permutation of the 26 characters of the alphabet')
    return value

@hug.type()
def type_key_square_size(value):
    """The size of the keysquare, if size=5, the keysquare uses 5^2 or 25 characters"""
    if not value.isdigit():
        raise ValueError('Must be a whole number')
    return value


class type_char_set(hug.types.length):
    def __init__(self, length):
        self.length = length

    @property
    def __doc__(self):
        return 'The set of characters to use, as a {0} character string'.format(self.length)

    def __call__(self, value):
        l = len(value)
        if length < self.lower:
            raise ValueError("'{0}' is shorter than {1}".format(value, self.length))
        if length >= self.upper:
            raise ValueError("'{0}' is longer than {1}".format(value, self.length))
        return value

class type_key_square(hug.types.length):
    def __init__(self, length, text=None):
        self.length = length
        self.text = text

    @property
    def __doc__(self):
        return 'The {0}keysquare, as a {1} character string'.format(self.text,self.length).replace('  ', ' ')

    def __call__(self, value):
        l = len(value)
        if length < self.length:
            raise ValueError("'{0}' is shorter than {1}".format(value, self.length))
        if length >= self.length:
            raise ValueError("'{0}' is longer than {1}".format(value, self.length))
        return value

class type_key_cube(hug.types.length):
    """They keycube, as a {0} character string"""
    def __init__(self, length):
        self.length = length


    def __call__(self, value):
        l = len(value)
        if length < self.lower:
            raise ValueError("'{0}' is shorter than {1}".format(value, self.length))
        if length >= self.upper:
            raise ValueError("'{0}' is longer than {1}".format(value, self.length))
        return value



