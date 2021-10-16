#문제 https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    #lottos = sorted(lottos)
    #win_nums = sorted(win_nums)
    max=0
    min=0
    cnt=0
    cnt0=0
    for i in range(len(win_nums)):
        if lottos[i]==0:
            cnt0=cnt0+1
        elif lottos[i]>0 and lottos[i]<=45:
            for w in win_nums:
                if w==lottos[i]:
                    cnt=cnt+1
    #cnt    0 1 2 3 4 5 6
    #min    7 6 5 4 3 2 1
    #min    6 6 5 4 3 2 1
    
    #max    min-cnt0
    min=7-cnt
    max=min-cnt0
    if min>6:
        min=6
    if max>6:
        max=6
    answer = [max,min]
    return answer

def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

