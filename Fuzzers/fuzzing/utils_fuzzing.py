import random

def flip_random_character(s:str)->str:
    """
    description: Returns input with a random bit flipped in a random position

    input: 
    s(str): string, where a random bit flipped in a random position

    output:
    return_string(str): string with random bit flipped in a random position
    """
    if s == "":
        return s

    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    new_c = chr(c ^ bit)
    # print("Flipping", bit, "in", repr(c) + ", giving", repr(new_c))
    return_string = s[:pos] + bytes(new_c, 'utf-8') + s[pos + 1:]
    return return_string

def insert_random_character(s:str)->str:
    """
    description: Returns input with a random character inserted

    input: 
    s(str): string, where a random character is inserted

    output:
    return_string(str): string with a random inserted character
    """
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return_string = s[:pos] + bytes(random_character, 'utf-8') + s[pos:]
    return return_string


def delete_random_character(s:str)->str:
    """
    description: Returns input with a random character deleted

    input: 
    s(str): string, where a random character deleted

    output:
    return_string(str): string with a random character deleted
    """
    if s == "":
        return s

    pos = random.randint(0, len(s) - 1)
    return_string =  s[:pos] + s[pos + 1:]
    return return_string