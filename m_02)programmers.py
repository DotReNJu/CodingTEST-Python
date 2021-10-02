def solution(array, commands):
    answer=[]
    for cmd in commands:
        ar2= array[cmd[0]-1:cmd[1]]
        ar2.sort()
        answer.append(ar2[cmd[2]-1])
    return answer
