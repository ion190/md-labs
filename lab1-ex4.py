# You have to write a program that computes the truth table for various expressions. The set of expressions are limited to:
# - `and` operation
# - `or` operation
# - `not` operation
# - supports parenthesis


from itertools import product
from prettytable import PrettyTable  # Install using: pip install prettytable


def evaluate_expression(expr, variable_values):
    """
    Evaluate a boolean expression given variable values.
    """
    expr = expr.replace('!', 'not ')
    for var, val in variable_values.items():
        expr = expr.replace(var, str(val))
    return int(eval(expr))


def generate_truth_table(expression, variables):
    """
    Generate the truth table for a boolean expression.
    """
    table = PrettyTable(variables + [expression, 'Result'])
    table.align = 'c'

    for values in product([0, 1], repeat=len(variables)):
        row = list(values)
        row.append(evaluate_expression(expression, dict(zip(variables, values))))
        row.append(evaluate_expression(expression, dict(zip(variables, values))))
        table.add_row(row)

    return table


def main():
    expression = input("Enter a boolean expression: ")

    # Extracting variables from the expression and sorting them
    variables = sorted(list(set(filter(str.isalpha, expression))))

    # Generating and displaying the truth table
    truth_table = generate_truth_table(expression, variables)
    print(truth_table)


if __name__ == "__main__":
    main()
