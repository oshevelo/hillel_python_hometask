from datetime import date, timedelta


def calc_exp(expression):
    """Возведение в степень"""
    mult_index = expression.index('^')
    res = expression[mult_index-1] ** expression[mult_index+1]
    del expression[mult_index-1:mult_index+2]
    expression.insert(mult_index-1, res)
    return expression


def calc_mult(expression):
    """Умножение"""
    mult_index = expression.index('*')
    res = expression[mult_index-1] * expression[mult_index+1]
    del expression[mult_index-1:mult_index+2]
    expression.insert(mult_index-1, res)
    return expression


def calc_div(expression):
    """Деление"""
    mult_index = expression.index('/')
    res = expression[mult_index-1] / expression[mult_index+1]
    del expression[mult_index-1:mult_index+2]
    expression.insert(mult_index-1, res)
    return expression


def calc_sum(expression):
    """Сложение"""
    mult_index = expression.index('+')
    if type(expression[mult_index-1]) == date:
        res = expression[mult_index-1] + timedelta(days=int(expression[mult_index+1]))
    else:
        res = expression[mult_index-1] + expression[mult_index+1]
    del expression[mult_index-1:mult_index+2]
    expression.insert(mult_index-1, res)
    return expression


def calc_sub(expression):
    """Вычитание"""
    mult_index = expression.index('-')
    if type(expression[mult_index-1]) == date:
        res = expression[mult_index-1] - timedelta(days=int(expression[mult_index+1]))
    else:
        res = expression[mult_index-1] + expression[mult_index+1]
    del expression[mult_index-1:mult_index+2]
    expression.insert(mult_index-1, res)
    return expression
