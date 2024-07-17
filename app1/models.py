from django.db import models
from django.core.validators import RegexValidator
import datetime

# Create your models here.
alpha_validator = RegexValidator(
    regex=r'^[a-zA-Z]*$',
    message='Only alphabetic characters are allowed.'
)
integer_validator = RegexValidator(
    regex=r'^[0-9]+$',
    message='Enter only integer.'
)
special_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9]+$',
    message='Enter proper PaperCode.'
)
                #BatchMaster table-------->>>>>>>>>
batch=((" ","Select_Batch"),("2020-2022","2020-2022"),
       ("2021-2023","2021-2023"),("2022-2024","2022-2024"),
       ("2023-2025","2023-2025"),("2024-2025","2024-2025"),
       ("2025-2027","2025-2027"),("2026-2028","2026-2028"),
       ("2027-2029","2027-2029"),("2028-2030","2028-2030"))

class BatchMaster(models.Model):
    #batchno=models.IntegerField(default=0)
    batchno = models.CharField(max_length=3,validators=[integer_validator])
    batchid= models.CharField(max_length=10,choices=batch,default=" ") 
    #batchid=models.CharField(max_length=20)       
    def __str__(self):
        res= self.batchid
        return str(res)
papertype=((" ","select PaperType"),
           ("CompulFoundation","CompulFoundation"),("Core","Core"),
           ("Generic Elective","Generic Elective"),("lab","lab"),
           ("open Elective","open Elective"),("compulsory","compulsory"))
class PaperMaster(models.Model):
    papercode=models.CharField(max_length=8,validators=[special_validator])
    papertype=models.CharField(max_length=20,choices=papertype,default=" ")
    papersheetname=models.CharField(max_length=10, validators=[alpha_validator])
    papername=models.CharField(max_length=25, validators=[special_validator])    
    def __str__(self):
        res= self.papercode
        return str(res)

    '''papername=models.CharField(max_length=60)
    papercode=models.CharField(max_length=60)
    papertype=models.CharField(max_length=60)
    papersheetname=models.CharField(max_length=60)
    def __str__(self):
        return self.papername'''
class CourseMaster(models.Model):
    #course=models.CharField(max_length=5)      
    #courseid=models.IntegerField(default=0) 
    course=models.CharField(max_length=5,validators=[alpha_validator])
    courseid=models.CharField(max_length=5,validators=[integer_validator])
    
    def __str__(self):
        res= self.course
        return str(res)
    #def __str__(self):
        #return self.course 
sem=((" ","select_semister"),
     ("First","First"),
     ("Second","Second"),
     ("Third","Third"),
     ("Fourth","Fourth"))        
class SemMaster(models.Model):
    #semid=models.IntegerField(default=0)
    #sem=models.CharField(max_length=4)   
    sem=models.CharField(max_length=15,choices=sem,default=" ")
    semid=models.CharField(max_length=6, validators=[integer_validator])
    
    def __str__(self):
        res= self.sem 
        return str(res)    
    #def __str__(self):
        #return self.sem  
type=((" ","select-ExamType"),
     ("Internal-I","Internal-I"),
     ("Internal-II","Internal-II"),
     ("External","External"))
class ExamMaster(models.Model):
    examid=models.CharField(max_length=6, validators=[integer_validator])
    examtype=models.CharField(max_length=15, choices=type,default=" ")

    def __str__(self):
        res= self.examtype
        return str(res)
    
    '''examid=models.IntegerField(default=0)
    examtype=models.CharField(max_length=60)
    def __str__(self):
        return self.examtype'''
class StudentMaster(models.Model):
    batchno=models.ForeignKey(BatchMaster,on_delete=models.CASCADE,default=1)
    sem=models.ForeignKey(SemMaster,on_delete=models.CASCADE,default=1)
    course=models.ForeignKey(CourseMaster,on_delete=models.CASCADE,default=1)
    studentregno=models.CharField(max_length=6, validators=[integer_validator])
    studentname=models.CharField(max_length=25, validators=[alpha_validator])
    

    def __str__(self):
        res=self.studentname
        return str(res)
    '''studentname=models.CharField(max_length=60)
    course=models.ForeignKey(CourseMaster, on_delete=models.CASCADE, default=1)
    sem=models.ForeignKey(SemMaster, on_delete=models.CASCADE, default=1)
    studentregno=models.IntegerField(default=0)
    batchno=models.ForeignKey(BatchMaster, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.studentname'''
class Transaction(models.Model):
    course=models.ForeignKey(CourseMaster,on_delete=models.CASCADE)
    batch_no=models.ForeignKey(BatchMaster,on_delete=models.CASCADE)
    semester=models.ForeignKey(SemMaster,on_delete=models.CASCADE)
    exam_type=models.ForeignKey(ExamMaster,on_delete=models.CASCADE)
    student_name=models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    #student_reg_no=models.ForeignKey(StudentMaster,on_delete=models.CASCADE)
    #paper_code=models.ForeignKey(PaperMaster,on_delete=models.CASCADE)
    paper_name=models.ForeignKey(PaperMaster, on_delete=models.CASCADE)
    marks=models.CharField(max_length=3, validators=[integer_validator])

    def __str__(self):
        res= self.student_reg_no
        return str(res)
    '''course=models.ForeignKey(CourseMaster, on_delete=models.CASCADE, default=1)
    batch_no=models.ForeignKey(BatchMaster, on_delete=models.CASCADE, default=1)
    semester=models.ForeignKey(SemMaster, on_delete=models.CASCADE, default=1)
    exam_type=models.ForeignKey(ExamMaster, on_delete=models.CASCADE, default=1)
    student_name=models.ForeignKey(StudentMaster, on_delete=models.CASCADE, default=1)
    #student_reg_no=models.ForeignKey(StudentMaster, on_delete=models.CASCADE, default=1)
    paper_name=models.ForeignKey(PaperMaster, on_delete=models.CASCADE, default=1)
    #paper_code=models.ForeignKey(PaperMaster, on_delete=models.CASCADE, default=1)
    marks=models.IntegerField(default=0)'''
 

class EmployeeModel(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10,unique=True)
    email=models.EmailField()
    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)
