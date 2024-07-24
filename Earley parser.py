grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the']],
    'N': [['cat'], ['dog']],
    'V': [['chased'], ['saw']]
}

tokens = ['the', 'cat', 'chased', 'the', 'dog']
chart = [set() for _ in range(len(tokens) + 1)]
start_rule = ('S', ('NP', 'VP'), 0, 0)
chart[0].add(start_rule)

i = 0
while i <= len(tokens):
    added = True
    while added:
        added = False
        for state in list(chart[i]):
            lhs, rhs, dot, start = state

            if dot < len(rhs):
                next_symbol = rhs[dot]

                if next_symbol in grammar:
                    for production in grammar[next_symbol]:
                        new_state = (next_symbol, tuple(production), 0, i)
                        if new_state not in chart[i]:
                            chart[i].add(new_state)
                            added = True

                elif i < len(tokens) and tokens[i] == next_symbol:
                    new_state = (lhs, rhs, dot + 1, start)
                    if new_state not in chart[i + 1]:
                        chart[i + 1].add(new_state)
                        added = True

            else:
                for old_state in chart[start]:
                    old_lhs, old_rhs, old_dot, old_start = old_state
                    if old_dot < len(old_rhs) and old_rhs[old_dot] == lhs:
                        new_state = (old_lhs, old_rhs, old_dot + 1, old_start)
                        if new_state not in chart[i]:
                            chart[i].add(new_state)
                            added = True

    i += 1

# Print the chart
for idx, states in enumerate(chart):
    print(f"Chart[{idx}]:")
    for state in states:
        print(state)
