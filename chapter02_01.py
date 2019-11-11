# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model)
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
Point4 = namedtuple('Point','x y x class',rename = True) #Default -> False

print('EX2 - 1 ',Point1,Point2,Point3,Point4)
p1 = Point1(x = 10,y = 35)
p2 = Point2(20,40)
p3 = Point3(45,y = 20)
p4 = Point4(10,20,30,40)
# rename을 지원하기 때문에 Point4의 x가 중복된다. -> 이를 renaming해서 conflict를 피한다. 또한 class는 reserved word라서
# invalid syntax라서 _3으로 또 renaming한다
print('EX2-2 : ',p1,p2,p3,p4)
