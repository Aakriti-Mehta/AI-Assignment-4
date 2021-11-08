import re


def stack(X, Y):
    goal_stack.append('CLEAR('+Y+')')
    goal_stack.append('HOLD('+X+')')
    goal_stack.append('CLEAR('+Y+') , HOLD('+X+')')

    current_state.remove('CLEAR('+X+')')
    current_state.remove('HOLD('+X+')')

    current_state.append('AE')
    current_state.append('ON('+X+','+Y+')')


def unstack(X, Y):
    goal_stack.append('ON('+X+','+Y+')')
    goal_stack.append('CLEAR('+X+')')
    goal_stack.append('AE')
    goal_stack.append('ON('+X+','+Y+') , CLEAR('+X+') , AE')

    current_state.remove('ON('+X+','+Y+')')
    current_state.remove('AE')

    current_state.append('HOLD('+X+')')
    current_state.append('CLEAR('+Y+')')


def pickup(X):
    goal_stack.append('ONT('+X+')')
    goal_stack.append('CLEAR('+X+')')
    goal_stack.append('AE')
    goal_stack.append('ONT('+X+') , CLEAR('+X+') , AE')

    current_state.remove('ONT('+X+')')
    current_state.remove('AE')

    current_state.append('HOLD('+X+')')


def putdown(X):
    goal_stack.append('HOLD('+X+')')

    current_state.remove('HOLD('+X+')')

    current_state.append('ONT('+X+')')
    current_state.append('AE')


initial_state = ['ON(B,A)', 'ONTABLE(A)', 'ONTABLE(C)',
                 'ONTABLE(D)', 'CLEAR(B)', 'CLEAR(C)', 'CLEAR(D)', 'ARMEMPTY']

goal_state = ['ON(B,D)', 'ON(C,A)', 'ONTABLE(D)',
              'ONTABLE(A)', 'CLEAR(B)', 'CLEAR(C)', 'ARMEMPTY']

current_state = []
goal_stack = []

TSUBG = []

for state in goal_state:
    if state in initial_state:
        TSUBG.append(state)
    else:
        goal_stack.append(state)

for state in goal_stack:
    TSUBG.append(state)

goal_stack.append(TSUBG)
print(goal_stack)

for goal in goal_stack:
    if type(goal) is not list:
        matched = re.match("ON\(", goal)
        matched = bool(matched)
        if matched == True:

    else:
        for subgoal in goal:
            matched = re.match("ON\(", subgoal)
            matched = bool(matched)
            if matched == True:

# is_match = bool(matched)
# print(is_match)
