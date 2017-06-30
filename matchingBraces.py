# 30.06.2017
# Hackerrank challenge to find if a string is formed with matching braces


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def isEmpty(self):
        return len(self.stack) == 0


def isMatchingBrace(opening, closing):
    if opening == "(" and closing == ")":
        return True
    elif opening == "[" and closing == "]":
        return True
    elif opening == "{" and closing == "}":
        return True
    return False


def checkBraces(s):
    opening = ["(", "[", "{"]
    stack = Stack()
    for brace in s:
        if brace in opening:
            stack.push(brace)
        else:
            if stack.isEmpty():
                return "NO"
            lastBrace = stack.pop()
            if not isMatchingBrace(lastBrace, brace):
                return "NO"
    if stack.isEmpty():
        return "YES"
    return "NO"


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    print(checkBraces(s))
