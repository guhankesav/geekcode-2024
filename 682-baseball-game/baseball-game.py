class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            
            if i not in ["+","D","C"]:
                stack.append(i)
            elif i == "+":
                stack.append(str(int(stack[-2]) + int(stack[-1])))
            elif i == "D":
                stack.append(str(int(stack[-1])*2))
            elif i == "C":
                stack.pop()
            else:
                print("Error unknown")
            print(stack)
        tot = 0
        for i in stack:
            tot += int(i)
        return tot
            
        