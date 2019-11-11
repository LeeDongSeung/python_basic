# class adnvaced!
# class method, instance method, static method

class Student(object):
    """
    Student Class
    Author : Lee Dong Seung
    Date : 2019.11.11
    """
    tuition= 1.0
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
        return "After tuition Id -> {}, fee : {}".format(self._id,self._tuition * Student.tuition)


