from __future__ import annotations
from typing import Dict, List
import csv
import querypy.Term as Term
import querypy.Item as Item
import querypy.Formula as Formula
import querypy.local_types as ltype

class Querypy:
    def __init__(self, data: Dict[Item.ItemId, Item.Item], terms: Dict[Item.ItemPropertyName, Term.VariableTerm], properties: List[Item.ItemPropertyName]):
        self.data  = data
        self.terms = terms
        self.properties = properties
    
    def __getitem__(self, key: Item.ItemId) -> Item.Item:
        return self.data[key]

    def get_term(self, propertyName: Item.ItemPropertyName) -> Term.VariableTerm:
        if propertyName in self.terms.keys():
            return self.terms[propertyName]
        else:
            raise KeyError("Unknown property name: " + propertyName)
    
    def get_data(self, item_id: Item.ItemId, prop: Item.ItemPropertyName) -> ltype.Number:
        return self[item_id][prop]
    
    def get_substitute_dict(self, primary_key: Item.ItemId) -> Term.SubstituteDict:
        return { prop: self.get_data(primary_key, prop) for prop in self.properties }
    
    def find(self, formula: Formula.Formula) -> List[Item.ItemId]:     
        return [
            item_id for item_id
            in self.data.keys()
            if formula.evaluate(self.get_substitute_dict(item_id))
        ]


def read_csv(filename: str, primary_key: Item.ItemId) -> Querypy:  
    with open(filename) as f:
        csv_dict_reader = csv.DictReader(f, skipinitialspace=True)
        properties = [ prop for prop in csv_dict_reader.fieldnames if prop != primary_key ]

        def produce_dict(row) -> Item.Item:
            return { prop: float(row[prop]) for prop in properties}

        data = {
            row[primary_key]: produce_dict(row)
            for row in csv_dict_reader
        }

        term_dict = { prop: Term.VariableTerm(prop) for prop in properties }

    return Querypy(data, term_dict, properties)
