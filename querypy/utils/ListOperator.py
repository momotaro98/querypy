from querypy.local_types import *


def progressive_comparison(vector: Vector, binary_function: BinaryFunction) -> bool:
    size = len(vector)
    if size in [0,1]:
        raise ValueError("To progressively compare, more than two elements are needed.")
    else:
        return not (False in [ binary_function(vector[i], vector[i+1]) for i in range(size - 1) ])