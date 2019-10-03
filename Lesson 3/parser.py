from datetime import date


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
    accumulator = ''

    for i in expression_str:
        if i.isdigit() or i == '.':
            accumulator += i
        elif i in available:
            if accumulator:
                a = accumulator.split('.')
                if len(a) == 1:
                    expression.append(int(accumulator))
                elif len(a) == 2:
                    expression.append(float(accumulator))
                elif len(a) == 3:
                    expression.append(date(int(a[2]), int(a[1]), int(a[0])))
                accumulator = ''
            if i == '(':
                open_bracket_counter += 1
            elif i == ')':
                open_bracket_counter -= 1
                if open_bracket_counter < 0:
                    raise Exception(ValueError, 'Invalid brackets')
            expression.append(i)
        else:
            raise Exception(ValueError, f'Unexpected symbol {i}')
    if accumulator:
        a = accumulator.split('.')
        if len(a) == 1:
            expression.append(int(accumulator))
        elif len(a) == 2:
            expression.append(float(accumulator))
        elif len(a) == 3:
            expression.append(date(int(a[2]), int(a[1]), int(a[0])))
    if open_bracket_counter != 0:
        raise Exception(ValueError, 'Invalid brackets')
    return expression
