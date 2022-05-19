# 2. 리스트 명은 List인 빈 리스트를 생성해주세요.

# 3. 첫 번째 반복문을 사용합니다.
# 이 반복문은 range()를 이용해 1부터 15까지 정수를 입력받을 수 있도록 범위를 정해주세요. 
# 또한 이 반복문 안에 반복문을 통해 입력받은 정수가 리스트의 요소로 
# 추가될 수 있도록 해주세요. 그리고 조건문을 통해 반복문이 15번 반복된다면
# print()문을 이용해 리스트가 출력될 수 있도록 해주세요.

List = []

for x in range(1,16):
    x = int(input("정수를 입력하세요 : "))
    List.append(x)


# 전역변수 지역변수(for 문에서만 사용가능)

for x in List:
    if (x % 2 == 0):
        List.remove(x)



for x in List:
    if (x % 3 == 0):
        List.remove(x)




List.pop(0)

List.insert(0,2)
List.insert(1,3)

print(List)
