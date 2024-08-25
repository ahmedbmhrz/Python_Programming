def as_integer(an_object):
    if isinstance(an_object, str):
        if an_object.lstrip('-').isdigit():
            return int(an_object)
    return None

def main():
    elements = ['20', 10, len, True, '-six', '-10', '0']
    
    for element in elements:
        print(as_integer(element))
