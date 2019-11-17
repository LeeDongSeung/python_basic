# python 
# magic method
# need to know !!!!!
# x = [1,2,3,4,5]
# for i,v in enumerate(x):
#     print("index is : {} and value is : {}".format(i,v))

# 참조1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2 : https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직메소드 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 매직메소드 기초 설명
# 이미 python에 만들어진 method를 의미한다!!!!!!!!!!!!
# python의 모든 것은 object라서 그러하다 object를 사용하는 이유는 method!
# 기본형
# int 또한 classe다.
print(int)

# 모든 속성 및 메소드 출력
# print(dir(int))
# print()
# print()

n = 100
a = 200
# print("{0:0x}".format(n))
# 사용
# +를 하면 __add__를 호출한다고 볼 수 있다.
# print('EX1-1 -', n + 200)
# print('EX1-2 -', n.__add__(200))
# print('EX1-3 -', n)
# print('EX1-4 -', n.__doc__)
# # __bool__(self)와 같다 bool(n)과 같다
# print('EX1-5 -', n.__bool__(), bool(n))
# print('EX1-6 - ', n * 100, n.__mul__(100))

# print()
# print()

# 클래스 예제1
class Student(object):
    """
    Author : Lee
    Date : 2019.11.17
    """
    def __init__(self,name,height):
        self._name = name
        self._height = height
    
    def __str__(self):
        return "Student name is {} and height is {}".format(self._name,self._height)

    # class의 >=를 overloading!!
    def __ge__(self, x):
        print("Called . >> __ge__Method")
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self,x):
        print("Called . >> __le__Method")
        if self._height <= x._height:
            return True
        else:
            return False

    def __add__(self,x):
        print("Called . >> __add__Method")
        return self._height+x._height
    
    def __sub__(self,x):
        print("Called . >> __sub__Method")
        return self._height - x._height
        
# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)
# # 매직메소드 출력
print('EX2-1 -', s1 >= s2)
print('EX2-2 -', s1 <= s2)

print('EX2-3 -', s1 - s2)
print('EX2-4 -', s2 - s1)
print('EX2-5 - ', s1)
print('EX2-6 - ', s2)

# print()
# print()

# 클래스 예제2

class Vector(object):
    """
    Author:Lee
    """
    def __init__(self, *args):
        """create a vector example : v = Vector(1,2)"""
        if len(args) <= 1:
            self._x = 0
            self._y = 0
        # else:
        #     self._x = args[0]
        #     self._y = args[1]
        else:
            self._x,self._y = args
    def __repr__(self):
        """hoho"""
        return "Vector(%r,%r)" % (self._x,self._y)
    
    def __add__(self,x):
        """vector add"""
        return Vector(self._x+x._x,self._y+x._y)

    def __mul__(self, x):
        """vector add"""
        return Vector(self._x*x._x,self._y*x._y)
    # overloading!!!!    
    def __mul__(self, x:int):
        """vector add"""
        return Vector(self._x*x,self._y*x)

    def __bool__(self):
        return bool(max(self._x,self._y))
# Vector 인스턴스 생성
v1 = Vector(3,5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직메소드 출력
print('EX3-1 -', Vector.__init__.__doc__)
print('EX3-2 -', Vector.__repr__.__doc__)
print('EX3-3 -', Vector.__add__.__doc__)
print('EX3-4 -', v1, v2, v3)
print('EX3-5 -', v1 + v2)
print('EX3-6 -', v1 * 4)
print('EX3-7 -', v2 * 10)
print('EX3-8 -', bool(v1), bool(v2))
print('EX3-9 -', bool(v3))

# print()
# print()



# # 참고 : 파이썬 바이트 코드 실행
# import dis
# dis.dis(v2.__add__)