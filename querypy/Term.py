from typing  import Union, Dict
from querypy.Formula import Formula, FormulaType, Relations
from querypy.Item    import ItemPropertyName
from querypy.local_types import *

SubstituteDict = Dict[ItemPropertyName, Number]

class VariableTerm:
    def __init__(self, propertyName: ItemPropertyName):
        self.propertyName = propertyName

    def __lt__(self, term: 'Term') -> Formula:
        return Formula(FormulaType.ATOMIC, [], Relations.Less, [self, term])

    def __gt__(self, term: 'Term') -> Formula:
        return Formula(FormulaType.ATOMIC, [], Relations.Greater, [self, term])
    
    def __eq__(self, term: 'Term') -> Formula:
        return Formula(FormulaType.ATOMIC, [], Relations.Equal, [self, term])
    
    def substitute(self, substitute_dict: SubstituteDict) -> Number:
        if self.propertyName in substitute_dict:
            return substitute_dict[self.propertyName]
        else:
            raise KeyError("Given substitution does not cover: " + self.propertyName)

Term = Union[VariableTerm, int, float]

def substitute_terms(terms: List[Term], substitute_dict: SubstituteDict) -> List[Number]:
    def subs(term: Term) -> Number:
        if isinstance(term, VariableTerm):
            return term.substitute(substitute_dict)
        else:
            return term
    return [ subs(term) for term in terms ]
