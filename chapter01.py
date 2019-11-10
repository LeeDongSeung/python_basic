# class adnvaced!
 
# # 학생1
# student_name_1 = "kim"
# student_number_1 = 1
# student_grade_1 = 1
# student_detail_1 = [
#     {'gender':'Male'},
#     {'score1': 99},
#     {'score2':88}
# ]
# #학생 2
# student_name_2 = "Lee"
# student_number_2 = 2
# student_grade_2 = 2
# student_detail_2 = [
#     {'gender':'Female'},
#     {'score1': 59},
#     {'score2':88}
# ]
# #학생 3
# student_name_3 = "Park"
# student_number_3 = 3
# student_grade_3 = 3
# student_detail_3 = [
#     {'gender':'Male'},
#     {'score1': 99},
#     {'score2':38}
# ]


# # 리스트 구조
# # 굉장히 관리하기 힘들다.
# # 데이터의 정확한 위치(index)에 해당하는 data를 알아야 한다.
# student_names_list= ['kim','lee','park']
# student_numbers_list  =[1,2,3]
# student_grades_list = [1,2,4]
# student_details_list =[
#     {'gender':'Male','score1': 99,'score2':88},
#     {'gender':'Female','score1': 59,'score2':88},
#     {'gender':'Male','score1': 99,'score2':38}
# ]

# # 학생 삭제
# del student_names_list[1]
# del student_numbers_list[1]
# del student_grades_list[1]
# del student_details_list[1]

# print(student_names_list)
# print(student_numbers_list)
# print(student_grades_list)
# print(student_details_list)

# print(end='\n\n\n')

# # dictionary!
# # 코드 반복이 지속, 중첩 문제도 존재
# # db에서 많이 쓰임. 이러한 db 영역은 third-party(외부에서 제공하는 interface)

# students_dicts = [
#     {'student_name':'kim','student_number':1,'student_grade':1,'student_detail':{'gender':'Male','score1': 99,'score2':88}},
#     {'student_name':'lee','student_number':2,'student_grade':2,'student_detail':{'gender':'Female','score1': 59,'score2':88}},
#     {'student_name':'park','student_number':3,'student_grade':4,'student_detail':{'gender':'Male','score1': 99,'score2':100}}
# ]

# # del students_dicts[1]
# print(students_dicts)
# print(students_dicts[2].get('student_detail',None).get('score1',None))

# class로 바꿔보지!
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, method 활용
# 모든 class는 object를 상속!
class Student(object):

    def __init__(self,name,number,grade,details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
    # class의 이름을 부른다면 __str__를 call한다.
    # 그냥 print(class)하면 이렇게 __str__를 찍는다.
    def __str__(self):
        return 'str : {} - {}'.format(self._name,self._grade)
    # 둘의 차이는 무엇인가?
    # representation of the object!
    def __repr__(self):
        return 'repr : {} - {}'.format(self._name,self._grade)


student1 = Student('kim',1,1,{'gender':'Female','score1': 59,'score2':88})
student2 = Student('lee',2,2,{'gender':'Male','score1': 99,'score2':88})
student3 = Student('park',4,4,{'gender':'Male','score1': 19,'score2':88})
# python의 모든 객체는 이렇게 고유의 namespace를 가지고 있다.
# dictionary기반의 namespace를 가지고 있다
# constructor로 넘긴 parameter가 모두 나온다!


# list선언
student_list = []
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)
# 그냥 object i를 찍으면 __str__를 자동으로 부른다.
# overriding이다. 왜냐하면 obj의 __str__의 superclass를 하는 것이 아니기 때문에
for i in student_list:
    print(repr(i))

# 정리
# 
