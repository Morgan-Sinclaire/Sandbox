def balanced(parens):
    """
    Given a string that includes ()[]{} characters, determine if the
    parentheses are balanced by making a stack of the parentheses seen
    so far, and popping off appropriately.
    """
    s = []
    for i in range(len(parens)):
        if parens[i] in '(){}[]':
            s.append(parens[i])
        if s[-2:] in [['(', ')'], ['[', ']'], ['{', '}']]:
            s.pop(); s.pop();

    return not s    # balanced iff stack is empty

# print(balanced('([{}])'))
# print(balanced('{}()[](())'))
#
# tests taken from https://phoxis.org/2011/02/27/balanced-parenthesis-check/
# print(balanced('[{()[{()}]}({})]'))
# print(balanced('{a+(b*c)+[d*e/{f^g}]/22}'))
# print(balanced('{a+(b*c+[d*e/{f^g}]/22}'))
# print(balanced('((()}'))
