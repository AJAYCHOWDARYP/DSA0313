class FiniteStateAutomaton:
    def __init__(self):
        self.current_state = 'start'
    def transition(self, input_char):
        if self.current_state == 'start':
            if input_char == 'a':
                self.current_state = 'got_a'
            else:
                self.current_state = 'start'
        elif self.current_state == 'got_a':
            if input_char == 'b':
                self.current_state = 'accept'
            elif input_char == 'a':
                self.current_state = 'got_a'
            else:
                self.current_state = 'start'
        elif self.current_state == 'accept':
            if input_char == 'a':
                self.current_state = 'got_a'
            else:
                self.current_state = 'start'
    def is_accept_state(self):
        return self.current_state == 'accept'
def main():
    fsm = FiniteStateAutomaton()
    input_string = input("Enter a string: ")
    for char in input_string:
        fsm.transition(char)
    if fsm.is_accept_state():
        print("String ends with 'ab'")
    else:
        print("String does not end with 'ab'")
if __name__ == "__main__":
    main()
