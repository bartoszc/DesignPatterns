# (1) Klasa abstrakcyjna dla wszystkich wyrażeń (Expression)
class Expression:
    def interpret(self, context):
        pass


# (2) Terminalne wyrażenie (TerminalExpression) dla liczby
class Number(Expression):
    def __init__(self, value):
        self._value = value

    def interpret(self, context):
        return self._value


# (3) Nieterminalne wyrażenie (NonTerminalExpression) dla dodawania
class Add(Expression):
    def __init__(self, left_expression, right_expression):
        self._left = left_expression
        self._right = right_expression

    def interpret(self, context):
        return self._left.interpret(context) + self._right.interpret(context)


# (4) Nieterminalne wyrażenie (NonTerminalExpression) dla odejmowania
class Subtract(Expression):
    def __init__(self, left_expression, right_expression):
        self._left = left_expression
        self._right = right_expression

    def interpret(self, context):
        return self._left.interpret(context) - self._right.interpret(context)


# Klient
if __name__ == "__main__":
    # Tworzenie wyrażenia: 5 + 3 - 2
    expression = Subtract(Add(Number(5), Number(3)), Number(2))

    # Interpretacja wyrażenia
    result = expression.interpret(1)
    print(result)  # Wypisuje: 6
