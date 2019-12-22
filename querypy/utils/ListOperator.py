from __future__ import annotations
import querypy.local_types as ltype


def progressive_comparison(vector: ltype.Vector, binary_function: ltype.BinaryFunction) -> bool:
    size = len(vector)
    if size in [0,1]:
        raise ValueError("To progressively compare, more than two elements are needed.")
    else:
        return all( binary_function(vector[i], vector[i+1]) for i in range(size - 1) )
