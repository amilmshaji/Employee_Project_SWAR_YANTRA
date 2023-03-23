
from django.shortcuts import render

# Create your views here.
from .models import Department_tbl, Employee_tbl


def Department(request):
    if request.method=="POST":
        depName=request.POST.get('depName')
        hod=request.POST.get('hod')
        departmentType=request.POST.get('departmentType')
        misCategory=request.POST.get('misCategory')
        departmentCode=request.POST.get('departmentCode')
        status=request.POST.get('status')
        dep=Department_tbl(depName=depName,hod=hod,departmentType=departmentType,misCategory=misCategory,departmentCode=departmentCode,status=status)
        dep.save()

    return render(request,'AddDepartment.html')


def Employee(request):
    departments=Department_tbl.objects.all()
    if request.method=="POST":
        accountType=request.POST.get('accountType')
        employeeType=request.POST.get('employeeType')
        softNumber=request.POST.get('softNumber')
        payrollNumber=request.POST.get('payrollNumber')
        employeeName=request.POST.get('employeeName')
        gender=request.POST.get('gender')
        joiningDate=request.POST.get('joiningDate')
        emailId=request.POST.get('emailId')
        dob=request.POST.get('dob')
        renewalType=request.POST.get('renewalType')
        designation=request.POST.get('designation')
        noticePeriodTime=request.POST.get('noticePeriodTime')
        nonSbecExpTime=request.POST.get('nonSbecExpTime')
        presbecExpTime=request.POST.get('presbecExpTime')
        approver=request.POST.get('approver')
        department=request.POST.get('departmentfield')
        print(department)
        location=request.POST.get('location')
        emergencyContactNumber=request.POST.get('emergencyContactNumber')
        qualification=request.POST.get('location')
        bloodGroup=request.POST.get('location')
        mobileNumber=request.POST.get('location')
        maritalStatus=request.POST.get('location')
        branch=request.POST.get('location')
        otherBranch=request.POST.get('location')
        # joiningDate=datetime.strptime(joiningDate,'%y-%m-%d').gate
        emp=Employee_tbl(accountType=accountType,employeeType=employeeType,softNumber=softNumber,payrollNumber=payrollNumber,employeeName=employeeName,
                         gender=gender,joiningDate=joiningDate,emailId=emailId,dob=dob,renewalType=renewalType,designation=designation,noticePeriodTime=noticePeriodTime,
                         nonSbecExpTime=nonSbecExpTime,presbecExpTime=presbecExpTime,approver=approver,department_id=department,location=location,
                         emergencyContactNumber=emergencyContactNumber,qualification=qualification,bloodGroup=bloodGroup,mobileNumber=mobileNumber,
                         maritalStatus=maritalStatus,branch=branch,otherBranch=otherBranch)
        emp.save()
    context={
        "departments":departments
    }
    return render(request,'AddEmployee.html',context)