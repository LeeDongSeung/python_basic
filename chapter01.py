# class adnvaced!
 
# 학생1
student_name_1 = "kim"
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender':'Male'},
    {'score1': 99},
    {'score2':88}
]
#학생 2
student_name_2 = "Lee"
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender':'Female'},
    {'score1': 59},
    {'score2':88}
]
#학생 3
student_name_3 = "Park"
student_number_3 = 3
student_grade_3 = 3
student_detail_3 = [
    {'gender':'Male'},
    {'score1': 99},
    {'score2':38}
]


# 리스트 구조
# 굉장히 관리하기 힘들다.
# 데이터의 정확한 위치(index)에 해당하는 data를 알아야 한다.
student_names_list= ['kim','lee','park']
student_numbers_list  =[1,2,3]
student_grades_list = [1,2,4]
student_details_list =[
    {'gender':'Male','score1': 99,'score2':88},
    {'gender':'Female','score1': 59,'score2':88},
    {'gender':'Male','score1': 99,'score2':38}
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print(end='\n\n\n')

# dictionary!
# 코드 반복이 지속, 중첩 문제도 존재
# db에서 많이 쓰임. 이러한 db 영역은 third-party(외부에서 제공하는 interface)

students_dicts = [
    {'student_name':'kim','student_number':1,'student_grade':1,'student_detail':{'gender':'Male','score1': 99,'score2':88}},
    {'student_name':'lee','student_number':2,'student_grade':2,'student_detail':{'gender':'Female','score1': 59,'score2':88}},
    {'student_name':'park','student_number':3,'student_grade':4,'student_detail':{'gender':'Male','score1': 99,'score2':100}}
]

# del students_dicts[1]
print(students_dicts)
print(students_dicts[2].get('student_detail',None).get('score1',None))

# 이것으로 마무리?
# 드디어 했다