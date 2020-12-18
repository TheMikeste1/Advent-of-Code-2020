def find_subequation(equation: str):
    start = equation.find('(')
    open_eq = 0
    i = 0
    for i, char in enumerate(equation[start:]):
        if char == '(':
            open_eq += 1
        elif char == ')':
            open_eq -= 1
        if open_eq == 0:
            break
    return equation[start + 1:i], i


def parse_equation(equation: str):
    parsed = []
    i = 0
    lhs = None
    while i < len(equation):
        char = equation[i]
        i += 1
        if char == ' ':
            continue
        if char.isnumeric():
            if lhs is not None:
                rhs = int(char)
                if parsed and parsed[-1] != '*':
                    parsed[-1] = [parsed[-1], '+', [lhs, '+', rhs]]
                else:
                    parsed.append([lhs, '+', rhs])
                lhs = None
            else:
                lhs = int(char)
        elif char != '+':
            if char != '(':
                if lhs is not None:
                    if parsed and parsed[-1] != '*':
                        parsed[-1] = [parsed[-1], '+', lhs]
                    else:
                        parsed.append(lhs)
                    lhs = None
                parsed.append(char)
            else:
                sub, j = find_subequation(equation[i - 1:])
                sub = parse_equation(sub)
                if lhs is not None:
                    if parsed and parsed[-1] != '*':
                        parsed[-1] = [parsed[-1], '+', [lhs, '+', sub]]
                    else:
                        parsed.append([lhs, '+', sub])
                    lhs = None
                else:
                    lhs = sub
                i += j
    if lhs is not None:
        if parsed and parsed[-1] != '*':
            parsed[-1] = [parsed[-1], '+', lhs]
        else:
            parsed.append(lhs)
    if len(parsed) == 1 and isinstance(parsed[0], list):
        parsed = parsed[0]
    return parsed


def parse_equations(equations):
    parsed_eqs = []
    for equation in equations:
        parsed = parse_equation(equation)
        parsed_eqs.append(parsed)
    return parsed_eqs


def apply_operand(op, lhs, rhs):
    if op == '+':
        return lhs + rhs
    elif op == '-':
        return lhs - rhs
    elif op == '*':
        return lhs * rhs
    elif op == '/':
        return lhs / rhs
    raise ArithmeticError(f"Unknown operand: '{op}'")


def evaluate_equation(equation):
    if isinstance(equation[0], int):
        total = equation[0]
    elif isinstance(equation[0], list):
        total = evaluate_equation(equation[0])
    else:
        raise ArithmeticError(f"Can't start equation with {equation[0]}!")

    op = None
    for val in equation[1:]:
        if isinstance(val, int):
            total = apply_operand(op, total, val)
        elif isinstance(val, str):
            op = val
        else:
            num = evaluate_equation(val)
            total = apply_operand(op, total, num)
    return total


def evaluate_equations(equations):
    values = []
    for equation in equations:
        value = evaluate_equation(equation)
        values.append(value)
    return values


with open("equations.txt", 'r') as file:
    equations = file.read().splitlines()

equations = parse_equations(equations)

values = evaluate_equations(equations)

print(sum(values))

exit(0)
