List = []

for x in range(0,15):
    x = int(input("정수를 입력하세요 : "))
    List.append(x)

print(List)


# 전역변수 지역변수(for 문에서만 사용가능)

for x in List:
    if (x % 2 == 0):
        List.remove(x)
print(List)


for x in List:
    if (x % 3 == 0):
        List.remove(x)
print(List)


List.pop(0)
print(List)
List.insert(0,2)
List.insert(1,3)

print(List)
