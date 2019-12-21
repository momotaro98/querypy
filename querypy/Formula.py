from __future__ import annotations
from typing import List
from enum   import Enum
import querypy.Term   as Term
import querypy.utils.ListOperator as Ope


class FormulaType(Enum):
    ATOMIC   = 0
    AND      = 1
    OR       = 2
    NOT      = 3
    CONSTANT = 4

class Relations(Enum):
    DummyRelation  = 0
    Greater        = 1
    Less           = 2
    GreaterOrEqual = 3
    LessOrEqual    = 4
    Equal          = 5

class Formula:
    def __init__(self, operator: FormulaType, operands: List[Formula], relation: Relations, terms: List[Term.Term], default_value: bool):
        self.operator = operator
        self.operands = operands
        self.relation = relation
        self.terms    = terms
        self.default_value = default_value
    
    def evaluate(self, substitute_dict: Term.SubstituteDict) -> bool:
        if self.operator == FormulaType.CONSTANT:
            return self.default_value
        elif self.operator == FormulaType.ATOMIC:
            numbers = Term.substitute_terms(self.terms, substitute_dict)
            if self.relation == Relations.Equal:
                return Ope.progressive_comparison(numbers, lambda x, y: x == y)
            elif self.relation == Relations.Greater:
                return Ope.progressive_comparison(numbers, lambda x, y: x > y)
            elif self.relation == Relations.GreaterOrEqual:
                return Ope.progressive_comparison(numbers, lambda x, y: x >= y)
            elif self.relation == Relations.Less:
                return Ope.progressive_comparison(numbers, lambda x, y: x < y)
            elif self.relation == Relations.LessOrEqual:
                return Ope.progressive_comparison(numbers, lambda x, y: x <= y)
            else:
                raise TypeError("Term's operator has to be " + type(Relations) + ", not " + type(self.operator))
                
        elif self.operator == FormulaType.AND:
            return not (False in [ f.evaluate(substitute_dict) for f in self.operands ])
        elif self.operator == FormulaType.OR:
            return (True  in [ f.evaluate(substitute_dict) for f in self.operands ])
        elif self.operands == FormulaType.NOT:
            if len(self.operands) == 1:
                return not self.operands[0].evaluate(substitute_dict)
            else:
                raise ValueError("Formula with NOT operator has to have exactly one operand, not" + str(self.operands))
        else:
            raise TypeError("Formula's operator has to be " + type(FormulaType) + ", not " + type(self.operator))
    
    def __and__(self, formula: Formula) -> Formula:
        return Formula(FormulaType.AND, [self, formula], Relations.DummyRelation, [], True)
    
    def __or__(self, formula: Formula)  -> Formula:
        return Formula(FormulaType.OR,  [self, formula], Relations.DummyRelation, [], True)
    
    def __not__(self, formula: Formula) -> Formula:
        return Formula(FormulaType.NOT, [self], Relations.DummyRelation, [], True)
    