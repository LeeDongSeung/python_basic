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

student1 = Student('kim',1,1,{'gender':'Female','score1': 59,'score2':88})
student2 = Student('lee',2,2,{'gender':'Male','score1': 99,'score2':88})
student3 = Student('park',4,4,{'gender':'Male','score1': 19,'score2':88})



