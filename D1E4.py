#OOPR-Exer-4
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_gender(self,gender):
        self.__gender=gender
    def get_gender(self):
        return self.__gender
a1=Athlete("Maria","girl")
a1.running()
a1.set_name("Maria")
a1.get_name()
a1.set_gender("girl")
a1.get_gender()

                                        
