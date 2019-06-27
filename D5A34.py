#OOPR-Assgn-34
class Company:
    #Stores hike% based on job level.
    dict_hike={"A":5, "B":6, "C":10 , "D":11}
    #Consider incentive provided in all classes to be in Rupees(Rs).
    __c_incentive=5000
    def __init__(self,name):
        self.name=name
    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive
class Employee:
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list):
        self.emp_id=emp_id
        self.__e_incentive=e_incentive
        self.__salary=salary
        self.__job_level=job_level
        self.__performance_list=performance_list
    def get_e_incentive(self):
        return self.__e_incentive
    def get_performance_list(self):
        return self.__performance_list
    def get_salary(self):
        return self.__salary
    def get_job_level(self):
        return self.__job_level
    def identify_performance_hike(self):
        return None
    def identify_job_level_hike(self):
        return None
    def identify_incentive(self):
        return None
    def update_salary(self,hike, incentive):
        self.__salary= (self.__salary+ self.__salary*hike/100) + incentive
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False
class PermanentEmployee(Employee):
    def __init__(self,emp_id,e_incentive,job_level,salary,performance_list,p_incentive):
        super().__init__(emp_id,e_incentive,job_level,salary, performance_list)
        self.__p_incentive=p_incentive
    def get_p_incentive(self):
        return self.__p_incentive
    def identify_performance_hike(self):
        val=super().get_performance_list()
        
        val1=val[::-1]
        print(val1)
        if val1[0]==1 and val1[1]==1:
            hike=5
        elif val1[0]==1 and val1[1]==2 and val1[2]==1:
            hike=3
        else:
            return None
        return hike
                                    
    def identify_job_level_hike(self):
        if super().get_job_level() in Company.dict_hike:
            return Company.dict_hike[super().get_job_level()]
        else:
            return None
    def identify_incentive(self):
        return self.__p_incentive+super().get_e_incentive()+Company.get_c_incentive()
        
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                
                hike+=(ex_hike)
            incentive=self.identify_incentive()
            self.update_salary((hike), incentive)
            return True
        else:
            return False
c=Employee(2134,1000,"A",130000,[1, 2, 1, 1, 1])
p=PermanentEmployee(2134,1000,"A",130000,[1, 2, 1, 3, 1],3000)
print(p.identify_performance_hike())
print(p.identify_job_level_hike())
print(p.identify_incentive())
print(p.calculate_salary())
    
    
    
