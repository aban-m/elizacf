import re

def evaluate_problem(problem: dict, conditions: dict) -> bool:
    ''' Evaluate a problem based on parsed conditions '''
    
    # Default values
    rating = problem.get('rating', 1400)
    solvers = problem.get('solvedCount', 20000)
    div = problem.get('div', None)
    index = problem.get('index', None)
    tags = set(problem.get('tags', []))  # Convert to set for easier checks

    # Evaluate conditions
    for op, value in conditions['rating']:
        if not eval(f'{rating} {op} {value}'):
            return False

    if conditions['solvers']:
        for op, value in conditions['solvers']:
            if not eval(f'{solvers} {op} {value}'):
                return False

    if conditions['div'] and not div in conditions['div']:
        return False

    if conditions['index'] and index not in conditions['index']:
        return False

    required_tags = set(tag for tag in conditions['tags'] if not tag.startswith('-'))
    excluded_tags = set(tag[1:] for tag in conditions['tags'] if tag.startswith('-'))
    if (required_tags and not required_tags.issubset(tags)): print('bad +tags'); return False
    if not tags.isdisjoint(excluded_tags): print('bad -tags'); return False
    
    return True

def parse_conditions(s: str) -> list:
    ''' Parse the input string and return a list of conditions '''
    conditions = {
        'rating': [],
        'solvers': [],
        'div': set(),
        'tags': [],
        'index': set()
    }

    s = s.lower().strip().replace('\n', ' ').replace('\t', ' ')
    length = len(s)
    s += ' '
    i = 0
    
    while i < length:
        if s[i] == ' ': i += 1; continue
        
        elif s[i:i+6] == 'rating' or s[i:i+7] == 'solvers':
            key = 'rating' if s[i:i+6] == 'rating' else 'solvers'
            i += len(key)
            op = ''
            val = ''

            while s[i] not in '<=>': i += 1
            op = s[i]

            while not s[i].isdigit(): i += 1

            buf = ''
            while s[i].isdigit():
                buf += s[i]
                i += 1
            val = int(buf)

            conditions[key].append((op, val))

        elif s[i] in '+-':
            tag = ''
            while s[i] != ' ':
                tag += s[i]
                i += 1
            conditions['tags'].append(tag.replace('_', ' '))

        elif s[i:i+3] == 'div':
            i += 3
            conditions['div'].add(int(s[i]))

        elif s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower():
            conditions['index'].add(s[i].upper())

        else:
            raise ValueError(f'Unrecognized token: {s[i]}.')

        i += 1

    return conditions
