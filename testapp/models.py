from django.db import models
#from testapp.views import Employee,Role,Department


# Create your models here.
class Department(models.Model):
     eno=models.IntegerField()
     ename=models.CharField(max_length=100)
     elocation=models.CharField(max_length=100)
     def __str__(self):
         return self.ename
    
class Role(models.Model):
     eno=models.IntegerField()
     ename=models.CharField(max_length=100)    
     def __str__(self):
         return self.ename
    
    
    

class Employee(models.Model) :
    eno=models.IntegerField()
    
    efirst_name=models.CharField(max_length=100, null=False)   
    elast_name = models.CharField(max_length=100)
    
    esal = models.FloatField()
    ebonus = models.IntegerField(default=0)  
    
    ephone = models.IntegerField(default=0)
    ehire_date = models.DateField()
    #edept=models.ForeignKey(Department,on_delete=models.CASCADE)

    #erole=models.ForeignKey(Role,on_delete=models.CASCADE) 
    elocation=models.CharField(max_length=100)
    def __str__(self):
         return '%s %s %s %s %s %s %s ' %(self.efirst_name,self.elast_name,self.ephone,self.esal,self.eno,self.ebonus,self.ehire_date)
    
    
    
    

