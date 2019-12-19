from __future__ import annotations
from typing  import Union, Dict, List
import querypy.Formula as Formula
import querypy.Item    as Item
import querypy.local_types as ltype

SubstituteDict = Dict[Item.ItemPropertyName, ltype.Number]

class VariableTerm:
    def __init__(self, propertyName: Item.ItemPropertyName):
        self.propertyName = propertyName

    def __lt__(self, term: 'Term') -> Formula.Formula:
        return Formula.Formula(Formula.FormulaType.ATOMIC, [], Formula.Relations.Less, [self, term])

    def __gt__(self, term: 'Term') -> Formula.Formula:
        return Formula.Formula(Formula.FormulaType.ATOMIC, [], Formula.Relations.Greater, [self, term])
    
    def __eq__(self, term: 'Term') -> Formula.Formula:
        return Formula.Formula(Formula.FormulaType.ATOMIC, [], Formula.Relations.Equal, [self, term])
    
    def substitute(self, substitute_dict: SubstituteDict) -> ltype.Number:
        if self.propertyName in substitute_dict:
            return substitute_dict[self.propertyName]
        else:
            raise KeyError("Given substitution does not cover: " + self.propertyName)

Term = Union[VariableTerm, int, float]

def substitute_terms(terms: List[Term], substitute_dict: SubstituteDict) -> List[ltype.Number]:
    def subs(term: Term) -> ltype.Number:
        if isinstance(term, VariableTerm):
            return term.substitute(substitute_dict)
        else:
            return term
    return [ subs(term) for term in terms ]
