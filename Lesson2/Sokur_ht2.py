def calc_substitute(expression_str):
    """
    Делает замену 'pi', 'e' на численные значения
    Делает замену '**' на одинарный знак '^'
    """
    expression_str = expression_str.replace('**', '^')
    expression_str = expression_str.replace('pi', '3.14')
    expression_str = expression_str.replace('e', '2.71')
    return expression_str


def calc_parser(expression_str):
    """
    Разбивает строку на список состоящий из Float чисел и допустимых символов
    Поднимает исключение при попадании недопустимого символа или некорректных скобок
    """
    expression = []
    available = ['*', '/', '^', '+', '-', '(', ')']
    open_bracket_counter = 0
    num_accumulator = ''

    for i in expression_str:
        if i.isdigit() or i == '.':
            num_accumulator += i
        elif i in available:
            if num_accumulator:
                expression.append(float(num_accumulator))
                num_accumulator = ''
            if i == '(':
                open_bracket_counter += 1
            elif i == ')':
                open_bracket_counter -= 1
                if open_bracket_counter < 0:
                    raise Exception(ValueError, 'Invalid brackets')
            expression.append(i)
        else:
            raise Exception(ValueError, f'Unexpected symbol {i}')
    if num_accumulator:
        expression.append(float(num_accumulator))
    if open_bracket_counter != 0:
        raise Exception(ValueError, 'Invalid brackets')
    return expression


def calc_exp(exppression):
    """Возведение в степень"""
    mult_index = exppression.index('^')
    res = exppression[mult_index-1] ** exppression[mult_index+1]
    del exppression[mult_index-1:mult_index+2]
    exppression.insert(mult_index-1, res)
    return exppression


def calc_mult(exppression):
    """Умножение"""
    mult_index = exppression.index('*')
    res = exppression[mult_index-1] * exppression[mult_index+1]
    del exppression[mult_index-1:mult_index+2]
    exppression.insert(mult_index-1, res)
    return exppression


def calc_div(exppression):
    """Деление"""
    mult_index = exppression.index('/')
    res = exppression[mult_index-1] / exppression[mult_index+1]
    del exppression[mult_index-1:mult_index+2]
    exppression.insert(mult_index-1, res)
    return exppression


def calc_sum(exppression):
    """Сложение"""
    mult_index = exppression.index('+')
    res = exppression[mult_index-1] + exppression[mult_index+1]
    del exppression[mult_index-1:mult_index+2]
    exppression.insert(mult_index-1, res)
    return exppression


def calc_sub(expression):
    """Вычитание"""
    mult_index = expression.index('-')
    res = expression[mult_index-1] - expression[mult_index+1]
    del expression[mult_index-1:mult_index+2]
    expression.insert(mult_index-1, res)
    return expression


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
        expression = calc_exp(expression)
    while '*' in expression:
        expression = calc_mult(expression)
    while '/' in expression:
        expression = calc_div(expression)
    while '+' in expression:
        expression = calc_sum(expression)
    while '-' in expression:
        expression = calc_sub(expression)
    return float(expression[0])


def calc(expression_str):
    expression = calc_substitute(expression_str)
    expression = calc_parser(expression)
    return calc_core(expression)


a = '(2+2)*2'
print(calc(a))
