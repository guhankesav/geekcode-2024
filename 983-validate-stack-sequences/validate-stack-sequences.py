class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        i, j = 0,0
        while i < len(pushed) and j < len(popped):
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j+=1
            stack.append(pushed[i])
            i+=1
        while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j+=1
        return True if not stack else False