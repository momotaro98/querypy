# Use

## Read Data

You can kickstart your analysis by
```py
from querypy import Querypy

data = Querypy.read_csv(<file_path>, <primary_key>)
```

So far, `Querypy` only accepts a very specific structure of CSV.
The input file should satisfy..

1. The first row of the CSV represents names of column (Header)
1. There is a single primary key
1. Except the primary key column, all the data are numbers

## Term: Identify Relevant Properties

Suppose that you have the following CSV input named `scores.csv`:
```csv
StudentName, Math101, Econ101
     Yamada,      80,      50
        Liu,      50,      80
```

Let us call each column like `Math101`, `Econ101`, `Comp101` as a property.
If you want to analyze property `Math101`, you should create a `Term` object with `get_term` method of the `Querypy` object.

```py
from querypy import Querypy

data    = Querypy.read_csv("scores.csv")
math101 = data.get_term("Math101")
econ101 = data.get_term("Econ101")
```

Just as the example, you can focus multiple numbers of properties by creating many corresponding terms.

## Formula: Create Logical Statements

`Formula` objects represent logical statements. Let's have a look at an example, where you want to see a student whose score is less than 59 in `Econ101`

(e.g.)
```
weakness_in_econ = econ101 < 59
```

Using operators `>`, `>=`, `<`, `<=`, `==`, you can create a single formula.
Other good and bad examples are:

```py
full_score_econ = econ101 == 100
pass_math_exam  = math101 >=  60

# You can contain multiple terms
better_in_math  = math101 > econ101

# You cannot put the term on the left size
pass_math_exam  = 60 <= math101 # -> Error!
```

You can create complex formulas by using `and`, `or`, `not`
```py
perfect = (math101 == 100) and (econ101 == 100)
```

## Find Records

`find` method of `Querypy` will return primary keys of records with given `Formula` objects in a `list` form.

```py
print(data.find(pass_math_exam))
# -> ['Liu']
print(data.find(full_score_econ))
# -> []
```

# Development Instruction

## Install dependencies

```
python3.8 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.lock
```

## Activate virtual environment

```
. venv/bin/activate
```

## Install a new package

```
. venv/bin/activate
pip install package_name
pip freeze | tee requirements.lock
```