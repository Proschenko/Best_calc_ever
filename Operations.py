class Operations:
    # нунунунунунунуннунгутмддытвятщывтоиолыпалпв
    @staticmethod
    def output(input_str: str):
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y
                     if y != 0 else 'Деление на ноль невозможно'}

        for operator in operators:
            if operator in input_str:
                operands = input_str.split(operator)
                try:
                    left, right = float(operands[0]), float(operands[1])
                    result = operators[operator](left, right)
                    return f'{result}'
                except ValueError:
                    return 'Ошибка: Невозможно преобразовать введенные значения в числа'
                except ZeroDivisionError:
                    return 'Ошибка: Деление на ноль невозможно'

        return 'Ошибка: Неподдерживаемый оператор'
