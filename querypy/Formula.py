from typing import List
from enum   import Enum
from querypy.Term   import Term, substitute_terms, SubstituteDict
from querypy.utils.ListOperator import progressive_comparison


class FormulaType(Enum):
    ATOMIC = 0
    AND    = 1
    OR     = 2
    NOT    = 3

class Relations(Enum):
    DummyRelation  = 0
    Greater        = 1
    Less           = 2
    GreaterOrEqual = 3
    LessOrEqual    = 4
    Equal          = 5

class Formula:
    def __init__(self, operator: FormulaType, operands: List['Formula'], relation: Relations, terms: List[Term]):
        self.operator = operator
        self.operands = operands
        self.relation = relation
        self.terms    = terms
    
    def evaluate(self, substitute_dict: SubstituteDict) -> bool:
        if self.operator == FormulaType.ATOMIC:
            numbers = substitute_terms(self.terms, substitute_dict)
            if self.relation == Relations.Equal:
                return progressive_comparison(numbers, lambda x, y: x == y)
            elif self.relation == Relations.Greater:
                return progressive_comparison(numbers, lambda x, y: x > y)
            elif self.relation == Relations.GreaterOrEqual:
                return progressive_comparison(numbers, lambda x, y: x >= y)
            elif self.relation == Relations.Less:
                return progressive_comparison(numbers, lambda x, y: x < y)
            elif self.relation == Relations.LessOrEqual:
                return progressive_comparison(numbers, lambda x, y: x <= y)
            else:
                raise TypeError("Term's operator has to be " + type(Relations) + ", not " + type(self.operator))
                
        elif self.operator == FormulaType.AND:
            return (False in [ f.evaluate(substitute_dict) for f in self.operands ])
        elif self.operator == FormulaType.OR:
            return (True  in [ f.evaluate(substitute_dict) for f in self.operands ])
        elif self.operands == FormulaType.NOT:
            if len(self.operands) == 1:
                return not self.operands[0].evaluate(substitute_dict)
            else:
                raise ValueError("Formula with NOT operator has to have exactly one operand, not" + str(self.operands))
        else:
            raise TypeError("Formula's operator has to be " + type(FormulaType) + ", not " + type(self.operator))
    
    def __and__(self, formula: 'Formula') -> 'Formula':
        return Formula(FormulaType.AND, [self, formula], Relations.DummyRelation, [])
    
    def __or__(self, formula: 'Formula')  -> 'Formula':
        return Formula(FormulaType.OR,  [self, formula], Relations.DummyRelation, [])
    
    def __not__(self, formula: 'Formula') -> 'Formula':
        return Formula(FormulaType.NOT, [self], Relations.DummyRelation, [])
    