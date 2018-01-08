import re


class Parser():
    RE_NUMBER = re.compile(r'^-?[0-9]+$')

    def __init__(self, tokens):
        self._current_index = 0
        self._start_node = None
        self._length = len(tokens)
        self._tokens = tokens
        self.node = None

    def end(self):
        return self._current_index == self._length - 1

    def peek(self):
        return self._tokens[self._current_index] if not self.end() else None

    def next(self):
        if not self.end():
            self._current_index += 1

    def parse(self):
        node = self._parse_e1()
        return node

    def _parse_e1(self):
        node = self._parse_e2()
        if self.peek() == "+":
            self.next()
            node2 = self._parse_e1
            node = AddNode(node, node2)
        return node


    def _parse_e2(self):
        node = self._parse_e3()
        if self.peek() == "*":
            self.next()
            node2 = self._parse_e2()
            node = MultNode(node, node2)
        return node

    def _parse_e3(self):
        if re.match(Parser.RE_NUMBER, self.peek()):
            node = LiteralNode(int(self.peek()))
        elif self.peek() == "(":
            self.next()
            node = self._parse_e1()
            if self.peek() != ")":
                raise Exception("(<e1> must be followed by a closing parentheses!")
        self.next()
        return node


class Node():

    def __init__(self, left, right):
        self._left = left
        self._right = right
        self._name = "cool"

    def evaluate(self):
        raise NotImplementedError()

class MultNode(Node):

    def evaluate(self):
        return self._left.evaluate() * self._right.evaluate()

class AddNode(Node):

    def evaluate(self):
        return self._left.evaluate() + self._right.evaluate()

class LiteralNode(Node):

    def __init__(self, value):
        super().__init__(None, None)
        self._value = value

    def evaluate(self):
        return self._value

your_calculator = Parser(["1", "+", "1"])
