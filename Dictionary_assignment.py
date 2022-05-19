Dic = {}

# Dic["somekey"] = input ("Enter a value")

while True:
    key = int(input("정수를 입력하세요"))
    
    value = input("문자열을 입력하세요")

    if key == 0 or value == '문자열 종료':
        break
    else:
        Dic[key]=value


print(list(Dic.keys()))
print(list(Dic.values()))
print(list(Dic.items()))