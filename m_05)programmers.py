#문제 https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3


def solution2(strings, n):
    answer = sorted(sorted(strings),key=lambda x:x[n])
    print(answer)
    return answer
