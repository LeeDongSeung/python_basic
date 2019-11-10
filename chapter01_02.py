# class adnvaced!
# Class Variable VS instance Variable!

class Student(object):
    """
    Student Class
    Author : Lee Dong Seung
    Date : 2019.11.10
    """
    # 클래스 변수, method 이외에서 scope를 가지는 변수!
    student_count = 0

    # intance variable!
    def __init__(self,name,number,grade,details,email = None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email
        # class이름으로 접근하는 것이 class variable!
        Student.student_count += 1
    # class의 이름을 부른다면 __str__를 call한다.
    # 그냥 print(class)하면 이렇게 __str__를 찍는다.
    def __str__(self):
        return 'str : {}'.format(self._name)
    # 둘의 차이는 무엇인가?
    # representation of the object!
    def __repr__(self):
        return 'repr : {}'.format(self._name)

    def detail_info(self):
        print('Current Id :{}'.format(id(self)))
        print('Student detail info {} {} {}'.format(self._name,self._email,self._details))
    def __del__(self):
        Student.student_count -= 1

# self의 의미
student1 = Student('kim',1,1,{'gender':'Female','score1': 59,'score2':88})
student2 = Student('lee',2,2,{'gender':'Male','score1': 99,'score2':88},'tmd@naver.com')
a = 34
b = a
print(id(student1))
print(id(student2))
# is는 reference를 비교한다. 즉 C에서 Pointer를 비교한다고 생각 할 수 있다.
# 이때 1,"abc"와 같은 literal은 자주 쓰이기 때문에 memory에 미리 할당해 놓아서 언제나 같은 곳을 가리킨다.
# 그러나 "this is the string"와 같은 자주 쓰이지 않는 string은 memory에 만들고 이를 할당하기 때문에 다른 reference를 가질 수 있다.
print(a is b)

print()


# dir & __dict__
# print(dir(student1))
# represent the value which instance has with it
# dir은 attribute와 method를 모두 보여준다 값은 보여주지 않는다.
print(student1.__dict__)
print(student2.__dict__)

print(end = '\n\n\n\n')
# Document String -> comment를 읽어 올 수 있다.
# Doctring
print(Student.__doc__)

# 실행
print(id(student1))
student1.detail_info()
# 이는 error! self가 parameter로 없다. self는 instance니까 Student는 class다!
# 그래서 parameter로 student1를 passing!
Student.detail_info(student1)

# 비교(원형을 알려준다)
print(id(student1.__class__) == id(student2.__class__))

# instance 변수의 값 확인
# 직접 접근을 지양한다.
# student1._name = 'hoho'
# 이렇게 하면 별로다. -> encapsulation이 필요하다
# class로 접근하는 class variable와 instance로 접근하는 variable이 같다.(id가)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 오늘 제일 중요!
# 이러면 student1의 namespace에 student_count가 없다 -> 상위(class variable or 부모 클래스)로 올라가서 student_count가 있는지 검색한다
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(student1.__dict__)
print(id(student1.student_count))
print(id(Student.student_count))

del student2
print(student1.student_count)
print(Student.student_count)

