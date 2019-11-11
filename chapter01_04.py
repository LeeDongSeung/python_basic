from chapter01_03 import Student

# 해당 script가 시작일 때 (entry일 떄)만 아래의 코드가 실행된다.
# 그래야 chpater01_03에 있는 코드가 실행이 되지 않는다
if __name__ == '__main__':
    st1 = Student.student_const(1,'lee','hoho','hoho@naver.com','1',400,4.3)
    print(st1.__dict__)



