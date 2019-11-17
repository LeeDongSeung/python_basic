# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model) -> namedtuple, structured model is recommended!
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크(data type) -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화, 모든 것이 객체다(int, str, list, dict, tuple, set, )
# 모든 객체 -> id, type -> value를 가지고 있다
# 파이썬 -> 일관성
# 일반적인 튜플 사용
# immutable!
# 0 : x, 1 : y
# need to label to specify, clarify!
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
from math import sqrt

line_len1 = sqrt((pt2[0]-pt1[0]) ** 2 + (pt2[1]-pt1[1] )** 2)
print('EX-1 : {}'.format(line_len1))

# NamedTuple 선언

from collections import namedtuple

# namedtuple 사용
# class라는 것을 강조하기 위해서 Capital!
# Point  = namedtuple('Point','x y')
# ['x','y']로 하면 member로 접근이 가능하다
# class를 마치 사용하는 듯한 접근방식을 보여주고 있다.

# 두점 선언했다!
Point = namedtuple('Point',['x', 'y'])

pt1 = Point(1.0,5.0)
pt2 = Point(2.5,1.5)
# 계산!
line_len2 = sqrt((pt2.x-pt1.x) ** 2 + (pt2.y-pt1.y )** 2)
print('EX-2 : {}'.format(line_len2))
print('EX-3 : {}'.format(line_len1==line_len2))
# list가 좋은거 같다!
Point1 = namedtuple('Point', ['x','y'])
Point2 = namedtuple('Point','x y')
Point3 = namedtuple('Point','x, y')
Point4 = namedtuple('Point','x y x class',rename = True) # Default -> False

print('EX2 - 1 ',Point1,Point2,Point3,Point4)
# dict unpacking!!!!!!
tmp_dic = {'x':30,'y':55}
p1 = Point1(x = 10,y = 35)
p2 = Point2(20,40)
p3 = Point3(45,y = 20)
p4 = Point4(10,20,30,40)
# 이러면 error tmp_dic자체를 x로 mapping해서 error, **를 붙혀서 dictionary를 unpacking한다!
p5 = Point3(**tmp_dic)
# rename을 지원하기 때문에 Point4의 x가 중복된다. -> 이를 renaming해서 conflict를 피한다. 또한 class는 reserved word라서
# invalid syntax라서 _3으로 또 renaming한다
print('EX2-2 : ',p1,p2,p3,p4,p5)
# index error조심!
print('EX-3 : ',p1[0]+p2[1])
print('EX-3 : ',p1.x+p2.y)

x,y = p3
print('EX3 - 2 : ',x+y)
print('EX3-3 ',p4._2+p4._3)

# namedtuple method!

temp = [52,38] # data container, sequence, iterator인 data structure!
# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print('EX4-1',p4)

# _fields
print('EX4-1',p1._fields,p2._fields,p3._fields,p4._fields)

# _asdict() : OrderedDict return
# ordereddict은 말 그대로 순서가 있는 dictionary라서 iter도 가능한데 넣는 순서대로 한다!
print('EX4-3 ',p1._asdict(),p4._asdict())
# print(p1._asdict())
# for k,v in p1._asdict().items():
#     print(k,v)
# _replace() : 수정 된 '새로운'(id가 변한다) object를 만들어서 assign!!!!!!
# print('EX4-4 ',p2._replace(y = 100))
print(end = '\n\n\n')

# list comprehension!
# 반 20명, 4개반 (A,B,C,D)
Classes = namedtuple('Classes',['rank','number'])
# group list
numbers = [str(x) for x in range(1,21)]
# numbers = []
# for i in range(1,21):
#     numbers.append(str(i))
# print(numbers)
ranks = 'A B C D'.split()

# list comprehension!!!!!
# rank가 A일 때 numbers가 1,20까지 모두 실행된다!
# rank가 B일 때 numbers가 1,20까지 모두 실행된다!
students = [Classes(r,n) for r in ranks for n in numbers]
print('EX5-1',len(students))
print('EX5-2',students[4].rank)

students2 = [Classes(r,n) for r in "A B C D".split() for n in [str(n) for n in range(1,21)]]
print('EX6-1',len(students2))
print('EX6-2',students2[4].rank)

for i in students2:
    print('EX7-1 ',i)