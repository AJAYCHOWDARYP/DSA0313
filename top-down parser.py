class Parser:
    def __init__(self, grammar, start_symbol):
        self.grammar = grammar
        self.start_symbol = start_symbol
        self.input = None
        self.pos = 0

    def parse(self, input_string):
        self.input = input_string
        self.pos = 0
        success = self._parse_symbol(self.start_symbol)
        if success and self.pos == len(self.input):
            return True
        else:
            return False

    def _parse_symbol(self, symbol):
        if symbol in self.grammar:
            for production in self.grammar[symbol]:
                old_pos = self.pos
                if all(self._parse_symbol(sym) for sym in production):
                    return True
                self.pos = old_pos
            return False
        else:
            return self._match_terminal(symbol)

    def _match_terminal(self, terminal):
        if self.pos < len(self.input) and self.input[self.pos] == terminal:
            self.pos += 1
            return True
        return False

# Example usage:
if __name__ == "__main__":
    # Define a simple grammar
    grammar = {
        'S': [['a', 'A']],
        'A': [['b'], ['c']]
    }
    start_symbol = 'S'

    parser = Parser(grammar, start_symbol)

    test_strings = ["ab", "ac", "a", "abc"]

    for test_string in test_strings:
        result = parser.parse(test_string)
        print(f"String '{test_string}': {'Accepted' if result else 'Rejected'}")
