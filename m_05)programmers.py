#문제 https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
#n번째 문자를 기준으로 정렬.
#기본적으로 오름차순 정렬.

testcase=[
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
    "sut",
    "sub",
    "suw",
    "sue",
    "suk",
    "suq",
    "suz",
    "suj",
    "suo",
    "sup",
    "aug",
    "but"]
testn=1

def solution(strings, n):
    answer=[]
    for t in range(len(strings)):
        strings[t] = strings[t][n]+strings[t]
    strings.sort()

    for t in range(len(strings)):
        answer.append(strings[t][1:])
    strings=answer
    print(strings)
    print(answer)
    return answer

def solution2(strings, n):
    answer = sorted(sorted(strings),key=lambda x:x[n])
    print(answer)
    return answer

def notsolution3(strings, n):
    answer = []
    strings=sorted(strings)
    tmp='';
    
    for s1 in range(len(strings)-1):
        for s2 in range(s1+1,len(strings)):
            if strings[s1][n]>strings[s2][n]:
                print("전",strings)
                tmp=strings[s1]
                strings[s1]=strings[s2]
                strings[s2]=tmp
                tmp=''
                print("후",strings)
                continue
    answer=strings

    print(answer)
    return answer

solution(testcase,testn)
solution2(testcase,testn)




isChange=[1,2,3,4,5]
def ChangeIt(go):
    go.sort(reverse=True)
    go.append(go[0])
    go.sort(key=lambda x:x*-1)
    go.sort(key=lambda x:(x-3)*(-1))

ChangeIt(isChange)
print(isChange)











#notsolution3(testcase,testn)