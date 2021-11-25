'''
https://www.acmicpc.net/problem/9012 / 스택
https://www.acmicpc.net/problem/4949 / 스택
https://www.acmicpc.net/problem/2161 / 큐
https://programmers.co.kr/learn/courses/30/lessons/42584 / 스택 심화

'''
def solution():
    stack=[]
    yesno="YES"

    str=input()
    for i in range(len(str)):
        if str[i]=="(":
            stack.append(i)
        if str[i]==")":
            if stack:
                stack.pop()
            else:
                yesno="NO"
                break
    if yesno=="NO" or stack:
        print("NO")
    else :
        print("YES")
    return 0

solution()