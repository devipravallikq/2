def isBalanced(word):
    stack = []
    for ele in word:
        if ele == '(':
            stack.append(ele)
        else:
            if len(stack) == 0:
                return False 
            else:
                stack.pop()
    if len(stack) == 0:
        return True 
    return False
 
 
word = "()("
#word = input()
result = isBalanced(word)
print(result)