#OOPR-Assgn-7
#Start writing your code here
'''Assignment 7:
Write a Python program to implement the class
chosen with its attributes and methods.
Note:
1.Consider all instance variables to be private and methods to be public
2.An instructor may have multiple technology skills, so consider instance variable,
technology_skill to be a list
3.check_eligibility(): Return true if eligibility criteria is satisfied by
the instructor. Else, return false
4.An instructor is allocated a course, if he/she satisfies the below two conditions:
    eligibility criteria:
        if experience is more than 3 years, average feedback should be 4.5 or more
        if experience is 3 years or less, average feedback should be 4 or more
    he/she should posses the technology skill for the course
5.allocate_course(technology): Return true if the course which requires the given technology
can be allocated to the instructor. Else, return false
6.Perform case sensitive string comparison
7.Represent few objects of the class, initialize instance variables using setter methods,
invoke appropriate methods and test your program.'''
class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__experience=None
        self.__technology_skill=None
        self.__avg_feedback=None
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
    def get_instructor_name(self):
        return self.__instructor_name
    def set_experience(self,experience):
        self.__experience=experience
    def get_experience(self):
        return self.__experience
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
    def get_technology_skill(self):
        return self.__technology_skill
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
    def get_avg_feedback(self):
        return self.__avg_feedback
    def check_eligibility(self):
        if(self.__experience>=3 and self.__avg_feedback>=4.5):
            return True
        elif(self.__experience<=3 and self.__avg_feedback>=4):
            return True
        else:
            return False
    def allocate_course(self,technology):
        #print(self.__technolofy_skill)
        if(self.check_eligibility()):
            if(technology in self.__technology_skill):
                return True
            else:
                return False
        else:
            return False
i1=Instructor()
i1.set_instructor_name("Priya")
#i1.get_instructor_name()
i1.set_experience(4)
#i1.get_experience()
i1.set_technology_skill(["Java","C","Python"])
#i1.get_technolofy_skill()
i1.set_avg_feedback(4.5)
#i1.get_avg_feedback())
i1.check_eligibility()
print(i1.allocate_course("Java"))


