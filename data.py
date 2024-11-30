import json
import random
from parsing import *

PROBLEMS = json.load(open('static/problems.json', 'r', encoding='utf-8'))
TEMPLATE = '''**{index}. {name}**{div_string}
{url}

Rating: **{rating}**
Tags: *{tag_string}*

Solved by: {solvedCount}
'''

def represent_problem(problem):
    kwargs = problem.copy()
    cid, ind = problem['contestId'], problem['index']
    kwargs['div_string'] = f'\nDiv. {problem["div"]}' if problem['div'] != -1 else ''
    kwargs['url'] = f'https://codeforces.com/contest/{cid}/problem/{ind}'
    kwargs['tag_string'] = ', '.join(problem['tags'])
    kwargs['solvedCount'] = problem.get('solvedCount', '(UNAVAILABLE)')
    return TEMPLATE.format(**kwargs)


def find(conditions, count=1):
    indices = random.sample(range(len(PROBLEMS)), len(PROBLEMS))
    out = []
    for ind in indices:
        if not count: break
        problem = PROBLEMS[ind]
        if evaluate_problem(problem, conditions):
            out.append(problem)
            count -= 1
    return out

##while True:
##    finds = find(parse_conditions(input('# ')))
##    if not finds: print("NOT FOUND"); continue
##    print(represent_problem(finds[0]))
##    print()
