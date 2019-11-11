# class adnvaced!
# class method, instance method, static method

class Student(object):
    """
    Student Class
    Author : Lee Dong Seung
    Date : 2019.11.11
    """
    tuition_per = 1.3
    def __init__(self, id,first_name, last_name,email, grade, tuition, gpa):
       self._id = id
       self._first_name = first_name
       self._last_name = last_name
       self._email = email
       self._grade = grade
       self._tuition = tuition
       self._gpa = gpa
   
    # Instance method
    def full_name(self):
        return "{} {}".format(self._first_name,self._last_name)
    # Instance method
    def detail_info(self):
        return "Student detail info : {} {} {} {} {} {}".format(self._id,self.full_name(),self._email,self._grade,self._tuition,self._gpa)
    # Instance method
    def get_fee(self):
        return "Before tuition Id -> {}, fee : {}".format(self._id,self._tuition)

    # instance_method
    def get_fee_calc(self):
        return "After tuition Id -> {}, fee : {}".format(self._id, self._tuition * Student.tuition_per)
    # magic method

    def __str__(self):
        return "student info -> name : {}, grade : {},email : {}".format(self.full_name(), self._grade, self._email)

    # class method! decorator!
    @classmethod
    def raise_fee(cls, per):
        try:
            if per < 1.0:
                raise ValueError
        except ValueError:
            print("tuition percent should be larger than 1!")
            return
        else:
            cls.tuition_per = per
            print('Succeed! tuition is increased!')

    # Class method로 init하는게 보다 pythonic grammar라고 볼 수 있다.
    # first argument cls -> class 그 자체다!
    @classmethod
    def student_const(cls,id,first_name, last_name,email, grade, tuition, gpa):
        return cls(id,first_name, last_name,email, grade, tuition * cls.tuition_per, gpa)

    # static method -> 누구나 쓸 수 있는 (self,cls를 parameter로 쓰지 않는다)
	# class or instance로도 접근이 가능하다

    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return "{} is a scholoarship recipient".format(inst._last_name)
        else:
            return "Sorry"



student_1 = Student(1,"kim","sarang","student1@naver.com",'1',400,3.5)
student_2 = Student(2,"lee","Myongho","student2@daum.net",'2',500,4.3)

# print(student_1)
# print(student_2)

# print(end='\n\n\n')

# print(student_1.detail_info())
# print(student_2.detail_info())

# 학비 정보
# print(student_1.get_fee())
# print(student_2.get_fee())

#class method 미사용
# class variable을 직접 접근하는 것은 지양해야 한다.
# Student.tuition_per = 1.4


# print(student_1.get_fee_calc())
# print(student_2.get_fee_calc())

Student.raise_fee(1.5)

# print(student_1.get_fee_calc())
# print(student_2.get_fee_calc())

# class method
student_3 = Student.student_const(3,'Park','minji','student3@gmail.com','3',550,4.5)
student_4 = Student.student_const(4,'Cho','sunghan','student3@gmail.com','4',600,4.1)

# # 전체 정보
# print(student_3.detail_info())
# print(student_4.detail_info())

# #학생 학비 변경
# print(student_3._tuition)
# print(student_4._tuition)

# static method!
# 클래스 안에서 분류를 원할 때, 학점을 기준으로 장학금 대상자인지 아닌지 파악하기 위함이다.
# parameter가 반드시 Student instance여야 한다
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return "{} is a scholoarship recipient".format(inst._last_name)
    else:
        return "Sorry"

print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))
print(end='\n\n\n')
print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))