class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if not (self.items == []):
            return self.items.pop()

    def top(self):
        if not (self.items == []):
            return self.items[-1]

    def size(self):
        return len(self.items)


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s = Stack()
        n = 0
        for i in expression:
            if i != ',' and i != ')':
                s.push(i)
            if i == ')':
                l = []
                while s.top() != '(':
                    l.append(s.top())
                    s.pop()
                s.pop()
                temp = s.top()
                s.pop()
                if temp == '&':
                    num = n
                    for j in l:
                        if j == 'f':
                            num += 1
                            break
                    e = 'f' if num == 1 else 't'
                    s.push(e)

                if temp == '|':
                    num = n
                    for j in l:
                        if j == 't':
                            num += 1
                            break
                    e = 't' if num == 1 else 'f'
                    s.push(e)

                if temp == '!':
                    e = 't' if l[0] == 'f' else 'f'
                    s.push(e)

        if s.top() == 't':
            return True
        else:
            return False


S = Solution()
print(S.parseBoolExpr("&(t,f,f)"))