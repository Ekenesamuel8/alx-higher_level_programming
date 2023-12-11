#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98            # LOAD_CONST 1 (98)
    result = result + a    # LOAD_FAST 0 (a) | BINARY_ADD
    result = result ** b   # LOAD_FAST 1 (b) | BINARY_POWER
    return result          # RETURN_VALUE



answer = magic_calculation(5, 2)
print (answer)
