d = {
    'q0': {
        'B': ['q1', 'B', 'R']
    },
    'q1': {
        '|': ['q1', 'A', 'R'],
        'B': ['q2', 'A', 'R']
    },
    'q2': {
        'A': ['q2', 'B', 'L'],
        'B': ['q2', 'B', 'L'],
        'a': ['q3', 'a', 'R'],
        'b': ['q3', 'b', 'R']
    },
    'q3': {
        'a': ['q3', 'a', 'R'],
        'b': ['q3', 'b', 'R'],
        'B': ['q4', 'A', 'L']
    },
    'q4': {
        'a': ['q4', 'a', 'L'],
        'b': ['q4', 'b', 'L'],
        'A': ['q5', 'A', 'R']
    },
    'q5': {
        'a': ['q6', 'A', 'L'],
        'b': ['q10', 'A', 'L']
    },
    'q6': {
        'A': ['q6', 'A', 'L'],
        'B': ['q7', 'B', 'R'],
        'a': ['q7', 'a', 'R'],
        'b': ['q7', 'b', 'R'],
    },
    'q10': {
        'A': ['q10', 'A', 'L'],
        'B': ['q11', 'B', 'R'],
        'a': ['q11', 'a', 'R'],
        'b': ['q11', 'b', 'R'],
    },
    'q7': {
        'A': ['q8', 'a', 'R']
    },
    'q11': {
        'A': ['q12', 'b', 'R']
    },
    'q8': {
        'A': ['q8', 'A', 'R'],
        'B': ['q9', 'B', 'L'],
        'a': ['q6', 'A', 'L'],
        'b': ['q10', 'A', 'L'],
    },
    'q12': {
        'A': ['q12', 'A', 'R'],
        'B': ['q9', 'B', 'L'],
        'a': ['q6', 'A', 'L'],
        'b': ['q10', 'A', 'L'],
    },
    'q9': {
        'A': ['q9', 'B', 'L'],
        'a': ['q9', 'a', 'L'],
        'b': ['q9', 'b', 'L'],
        'B': ['q9', 'B', 'L']
    }
}


def turing(d, cinta):
    print(f'cinta inicial: {cinta}\n')
    state = 'q0'
    cinta = list(cinta)
    posicion = 0
    i = 1
    while posicion >= 0:
        print(f"paso {i}:\n")
        print(''.join(cinta))
        print(posicion*' ' + '|')
        print(posicion*' ' + 'v')
        print(posicion*' ' + state + '\n')
        s, a, m = d[state][cinta[posicion]]
        state = s
        cinta[posicion] = a
        if m == 'R':
            posicion += 1
        elif m == 'L':
            posicion -= 1
        else:
            pass
        i += 1
    print(f'\ncinta final: {"".join(cinta)}')


turing(d, 'B||BbabaBB')
