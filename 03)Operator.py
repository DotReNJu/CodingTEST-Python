#Operator (연산자)

#산술연산자
print(5**2)
print(5%2)
print(5//2)
print(5/2)

#비교연산자
a=2
if a!=1:
    print("a는 1이아님",a,"임")

#할당연산자
a = a*10
a*=10
print(a)

#논리연산자
x=True
y=False
if x and y:
    print("Yes")
else:
    print("No")


#Bitwise 연산자
a=8
b=11
c=a&b
d=a^b

print(c)
print(d)