def isValid(s:   str) -> bool:
    stack = []
    open = {'(': 0, '{': 1, '[':2}
    closed = {')': 0, '}': 1, ']':2}
    for symb in s:
        if symb in open:
            stack.append(symb)
        elif symb in closed:
            if not stack or closed[symb] != open[stack.pop()]:
                return False

    return len(stack) == 0


