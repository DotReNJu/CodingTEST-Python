#문제 https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
#n번째 문자를 기준으로 정렬.
#기본적으로 오름차순 정렬.

def solution2(strings, n):
    answer = sorted(sorted(strings),key=lambda x:x[n])
    print(answer)
    return answer
