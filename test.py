conditions = []

if where_clause:

    for condition in where_clause.find_all(
        (exp.EQ, exp.GT, exp.GTE, exp.LT, exp.LTE, exp.In)
    ):
        conditions.append(condition.sql())

print(conditions)
