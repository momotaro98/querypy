from typing import Dict, List
import csv
from querypy.Term import VariableTerm, SubstituteDict
from querypy.Item import *
from querypy.Formula import Formula
from querypy.local_types import *

class Querypy:
    def __init__(self, data: Dict[ItemId, Item], terms: Dict[ItemPropertyName, VariableTerm], properties: List[ItemPropertyName]):
        self.data  = data
        self.terms = terms
        self.properties = properties
    
    def __getitem__(self, key: ItemId) -> Item:
        return self.data[key]

    def get_term(self, propertyName: ItemPropertyName) -> VariableTerm:
        if propertyName in self.terms.keys():
            return self.terms[propertyName]
        else:
            raise KeyError("Unknown property name: " + propertyName)
    
    def get_data(self, item_id: ItemId, prop: ItemPropertyName) -> Number:
        return self[item_id][prop]
    
    def find(self, formula: Formula) -> List[ItemId]:
        def get_substitute(item_id: ItemId) -> SubstituteDict:
            return {
                prop: self[item_id][prop] for prop in self.properties
            }
        
        return [
            item_id for item_id
            in self.data.keys()
            if formula.evaluate(get_substitute(item_id))
        ]


def read_csv(filename: str, id_row: ItemId) -> Querypy:  
    csv_dict_reader = csv.DictReader(open(filename))
    properties = [ prop for prop in csv_dict_reader.fieldnames if prop != id_row ]

    def produce_dict(row) -> Item:
        return { prop: row[prop] for prop in properties}
    
    data = {
        row[id_row]: produce_dict(row)
        for row in csv_dict_reader
    } 

    term_dict = { prop: VariableTerm(prop) for prop in properties }
    return Querypy(data, term_dict, properties)
