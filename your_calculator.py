import re


class Parser():
    RE_NUMBER = re.compile(r'^-?[0-9]+$')

    def __init__(self, tokens):
        self._current_index = 0
        self._start_node = None
        self._length = len(tokens)
        self._tokens = tokens

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
        pass

    def _parse_e2(self):
        pass

    def _parse_e3(self):
        pass


class Node():

    def __init__(self, left=None, right=None):
        self._left = left
        self._right = right
        self._name = "cool"

    def add_node(self, new_node):
        if self._left == None:
            self._left = new_node
        elif self._right == None:
            self._right = new_node
        else:
            raise IndexError("Attempting to add too many nodes!")

    def eval(self):
        raise NotImplementedError()

class MultNode(Node):

    def eval(self):
        return self._left.eval() * self._right.eval()

class AddNode(Node):

    def eval(self):
        return self._left.eval() + self._right.eval()

class LiteralNode(Node):

    def __init__(self, value):
        super().__init__(None, None)
        self._value = value

    def eval(self):
        return self._value

your_calculator = Parser(["1", "+", "1"])
