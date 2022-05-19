class Student:
    
    def __init__(self, name, grade, student_number, sex, address, phone_number, year):
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year

    def introduce(self): #클래스 내 메소드 명을 introduce 로 지정
        print("이름은 %s 이다." % self.name)
        print("학년은 %s 학년이다." % self.grade)
        print("학번은 %s 이다." % self.student_number)
        print("성별은 %s 이다." % self.sex)
        print("주소는 %s 이다" % self.address)
        print("전화번호는 %s 이다." % self.phone_number )
        if self.year == "1":  #if 를 이용해 "1"이 입력된다면 밑의 print문이 출력되는 조건문
            print("멋사 1년차")
            print(" 우와 아기사자다 !")
        else :
            print("멋사 %s년차" %self.year)
            print("우와 운영진이다 !")


while True: #while True 반복문을 이용해 객체 명이 "종료"가 되기 전까지 계속해서 입력을 받음.
    Class_name = input("객체 명을 입력하시오. (단, 영문으로) : ")
    if Class_name == "종료":
        break
        
    name = input("이름을 입력하시오. (단, 한글로) : ")
    grade = int(input("학년을 입력하시오. (단, 숫자로) :"))
    student_number = int(input("학번을 입력하시오. (단, 숫자로) : "))
    sex = input("성별을 입력하시오. (모를 때는 모른다 라고 입력.) :")
    if sex == "모른다":
        sex = "None"
    address = input("주소를 입력하시오. (~시까지만) :")
    phone_number = input("전화번호를 입력하시오 (모를 때는 모른다 라고 입력 : ")
    if phone_number == "모른다":
        phone_number = "None"
    year = input("멋사 몇년차인가요? (단, 숫자로) :")
        
    Class_name = Student(name, grade, student_number, sex, address, phone_number, year)
    Class_name.introduce()
