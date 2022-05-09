from datetime import datetime
from multiprocessing import context
from time import strftime
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
#from numpy import number



# Create your views here.
from testapp.models import Employee,Department,Role
# def department_info_view(request):
#      departments = Department.objects.all()
#      return render(request,'testapp/index.html',{'departments':departments})
# def role_info_view(request):
#      roles = Role.objects.all()
#      return render(request,'testapp/index.html',{'roles':roles})




# # Create your views here.
def employee_info_view(request):
      employees = Employee.objects.all()
      return render(request,'testapp/index.html',{'employees':employees})

def home_view(request):
    return render(request,'testapp/home.html')
def all_employee(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)

    
    return render(request,'testapp/all.html',context)



def add_employees_view(request):
    if request.method == 'POST':
       number=int(request.POST['eno']) 
       first_name=request.POST['efirst_name']
       last_name=request.POST['elast_name']
       sal=int(request.POST['esal'])
       bonus=int(request.POST['ebonus'])
       phone=int(request.POST['ephone'])
       #dept=int(request.POST['edept'])
       #role=int(request.POST['erole'])
       datetime=strftime(request.POST['ehire_date'])
       new_emp=Employee(ehire_date=datetime,eno=number,efirst_name=first_name, elast_name=last_name, esal=sal, ebonus=bonus,ephone=phone)
       new_emp.save( )
       return HttpResponse('Employee added successfully')
   
    elif request.method=='GET':  
      return render(request,'testapp/add.html')
    else:
       return HttpResponse('Exception occured! Employee has not been') 

def remove_employees_view(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee removed successfully')
        except:
            return HttpResponse('please enter a valid emp id')
            
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)

    
    
    
    return render(request,'testapp/remove.html',context)

def filter_employees_view(request):
    if request.method=='POST':
       first_name=request.POST['efirst_name']
       last_name=request.POST['elast_name']
    
       
       emps=Employee.objects.all()
       if first_name:
           emps=emps.filter(efirst_name__icontains=first_name)  
       if last_name:
           emps=emps.filter(elast_name__icontains=last_name)
         
       context = {
           'emps': emps
       }   
       
       return render(request,'testapp/all.html',context) 
    elif request.method=='GET':
        return render(request,'testapp/filter.html') 
    else:
        return HttpResponse('An exception occured')      
                  
       
        
    
    
    
    

