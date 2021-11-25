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
        print(yesno)
    else :
        print("YES")
    return 0

solution()