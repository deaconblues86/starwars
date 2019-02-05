from random import randint

def metric2imperial(val, start, dest):
    '''
    A simple function setup to convert cm to ft and kg to lb (and vice versa)
    - val: the value being converted
    - start: the starting unit of measure
    - dest: the target unit of measure
    Answer will be rounded to 2 decimal places
    '''

    conv = {
        "cm/ft": lambda x: x / 30.48,
        "ft/cm": lambda x: x * 30.48,
        "kg/lb": lambda x: x * 2.205,
        "lb/kg": lambda x: x / 2.205,
    }
    try:
        val = float(val)
    except ValueError:
        return val

    try:
        conv_func = conv[f"{start}/{dest}"]
    except KeyError:
        raise KeyError(f"Unknown unit conversion: {start} to {dest}")

    return round(conv_func(val), 2)


def rand_id():
    '''
    Generates a random interger from 1 to 87
    '''
    return randint(1, 87)
