#문제 https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
#n번째 문자를 기준으로 정렬.
#기본적으로 오름차순 정렬.

testcase=[[
    "sua",
    "bed",
    "car",
    "sux",
    "suc",
    "sud",
    "sug",
    "suh",
    "sul",
    "sum",
    "sub",
    "sut",
    "suw",
    "sue",
    "suk",
    "suq",
    "suz",
    "suj",
    "suo",
    "sup",
    "aug",
    "but"],
    1]

def solution(strings, n):
    answer = []
    strings=sorted(strings)
    tmp='';
    
    for s1 in range(len(strings)-1):
        for s2 in range(s1+1,len(strings)):
            if strings[s1][n]>strings[s2][n]:
                tmp=strings[s1]
                strings[s1]=strings[s2]
                strings[s2]=tmp
                tmp=''
                print(strings)
    answer=strings

    print(answer)
    return answer

def solution2(strings, n):
    answer = sorted(sorted(strings),key=lambda x:x[n])
    print(answer)
    return answer

solution(testcase)
solution2(testcase)