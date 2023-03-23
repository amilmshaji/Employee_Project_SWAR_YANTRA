from django.db import models

# Create your models here.



class Department_tbl(models.Model):
    depName= models.CharField(max_length=50,unique=True)
    hod=models.CharField(max_length=50)
    departmentType=models.CharField(max_length=50)
    misCategory=models.CharField(max_length=50)
    departmentCode=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)



class Employee_tbl(models.Model):
    accountType=models.CharField(max_length=50)
    employeeType=models.CharField(max_length=50)
    softNumber=models.CharField(max_length=50)
    payrollNumber=models.CharField(max_length=50)
    employeeName=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)


    joiningDate=models.DateField()


    emailId=models.CharField(max_length=50,unique=True)
    dob=models.DateField()
    renewalType=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    noticePeriodTime=models.IntegerField()
    nonSbecExpTime=models.IntegerField()
    presbecExpTime=models.IntegerField()
    approver=models.CharField(max_length=50)
    department=models.ForeignKey(Department_tbl,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    emergencyContactNumber=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    bloodGroup=models.CharField(max_length=50)
    mobileNumber=models.CharField(max_length=50)
    maritalStatus=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    otherBranch=models.CharField(max_length=50)

    def __str__(self):
        return self.employeeName

