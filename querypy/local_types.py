from typing import List, Union, Callable

Number = Union[int, float]
Vector = List[Number]
BinaryFunction = Callable[[Number, Number], bool]