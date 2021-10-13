#문제 https://programmers.co.kr/learn/courses/30/lessons/81301
#숫자 문자열과 영단어


def solution(s):
    s_num=['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = 0
    s_str=''
    tmp=''
    for ss in s:
        if ss.isalpha():
            tmp=tmp+ss
            if tmp in s_num:
                s_str=s_str+''+str(s_num.index(tmp))
                tmp=''
        elif ss.isdigit():
            s_str=s_str+''+ss
    answer=s_str
    print(answer)
    return int(answer)

def solution2(s):
    s_num=['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = 0
    for s_str in s_num:
        if s_str in s:
            s=s.replace(s_str,str(s_num.index(s_str)))
        answer=s
    print(answer)
    return int(answer)

def solution3(s):
    s_num=['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = 0
    for idx,num in enumerate(s_num):
        if num in s:
            s=s.replace(num,str(idx))
        answer=s

    print(answer)
    return int(answer)

solution("123tzeroest123zero")
solution2("123tzeroest123zero")

solution3("123tzeroest123zero")