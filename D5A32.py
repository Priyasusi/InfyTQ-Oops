from abc import ABCMeta,abstractmethod
class Employee(metaclass=ABCMeta):
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification
    def get_job_band(self):
        return self.__job_band
    def get_employee_name(self):
        return self.__employee_name
    def get_basic_salary(self):
        return self.__basic_salary
    def get_qualification(self):
        return self.__qualification
    @abstractmethod
    def validate_job_band(self):
        pass
    def validate_basic_salary(self):
        if(self.get_basic_salary()>3000):
            return True
        else:
            return False
        
    def validate_qualification(self):
        if(self.__qualification=="Bachelors" or self.__qualification=="Masters"):
            return True
        else:
            return False
        
    @abstractmethod
    def calculate_gross_salary(self):
        pass
class Graduate(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,cgpa):
        self.__cgpa=cgpa
        super().__init__(job_band,employee_name,basic_salary,qualification)
    def get_cgpa(self):
        return self.__cgpa
    def validate_job_band(self):
        if(self.get_job_band()=="A" or self.get_job_band()=="B" or self.get_job_band()=="C"):
            return True
        else:
            return False
    def calculate_gross_salary(self):
        if(self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band()):
            pf=self.get_basic_salary()*(12/100)
            if(self.__cgpa>=4 and self.__cgpa<=4.25):
                tpi_amount=1000
            elif(self.__cgpa>=4.26 and self.__cgpa<=4.5):
                tpi_amount=1700
            elif(self.__cgpa>=4.51 and self.__cgpa<=4.75):
                tpi_amount=3200
            elif(self.__cgpa>=4.76 and self.__cgpa<=5):
                tpi_amount=5000
            if(self.get_job_band().upper()=="A"):
                incentive=self.get_basic_salary()*(4/100)
            elif(self.get_job_band().upper()=="B"):
                incentive=self.get_basic_salary()*(6/100)
            elif(self.get_job_band().upper()=="C"):
                incentive=self.get_basic_salary()*(10/100)
            gross_salary=self.get_basic_salary()+pf+tpi_amount+incentive
            return gross_salary
        else:
            return -1
            
            
class Lateral(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
        self.__skill_set=skill_set
        super().__init__(job_band,employee_name,basic_salary,qualification)
    def get_skill_set(self):
        return self.__skill_set
    def validate_job_band(self):
        if(self.get_job_band()=="D" or self.get_job_band()=="E" or self.get_job_band()=="F"):
            return True
        else:
            return False
    def calculate_gross_salary(self):
        if(self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band()):
            pf=self.get_basic_salary()*(12/100)
            if(self.__skill_set=="AGP"):
                sme_bonus=6500
            elif(self.__skill_set=="AGPT"):
                sme_bonus=8200
            elif(self.__skill_set=="AGDEV"):
                sme_bonus=11500
            if(self.get_job_band().upper()=="D"):
                incentive=self.get_basic_salary()*(13/100)
            elif(self.get_job_band().upper()=="E"):
                incentive=self.get_basic_salary()*(16/100)
            elif(self.get_job_band().upper()=="F"):
                incentive=self.get_basic_salary()*(20/100)
            gross_salary=self.get_basic_salary()+pf+sme_bonus+incentive
            return gross_salary
        else:
            return -1
