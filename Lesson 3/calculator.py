import parser
import operations
from datetime import date


def calc_core(expression):
    """
    Функция выполняющая расчеты.
    Порядок выполнения действий по правилам вычислений.
    """

    while '(' in expression:
        open_index = expression.index('(')
        close_index = len(expression) - 1 - expression[::-1].index(')')
        res = calc_core(expression[open_index+1:close_index])
        del expression[open_index:close_index+1]
        expression.insert(open_index, res)

    while '^' in expression:
        expression = operations.calc_exp(expression)
    while '*' in expression:
        expression = operations.calc_mult(expression)
    while '/' in expression:
        expression = operations.calc_div(expression)
    while '+' in expression:
        expression = operations.calc_sum(expression)
    while '-' in expression:
        expression = operations.calc_sub(expression)
    if type(expression[0]) == date:
        return expression[0].strftime("%d.%m.%Y")#FIXME: test
    return expression[0]


def calc(expression_str):
    """

    :param expression_str:
        available symbols: '*', '/', '^', '+', '-', '(', ')'
        available constants: 'pi', 'e'
        available date format: 'dd.mm.yyyy'
    :return:
        result (date of float)
    """
    expression = parser.calc_substitute(expression_str)
    expression = parser.calc_parser(expression)
    return calc_core(expression)


a = '2.12.2000+2*4-1'
print(calc(a))
