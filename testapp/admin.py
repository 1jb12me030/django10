from django.contrib import admin

# Register your models here.
from testapp.models import Employee,Department,Role

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['eno','ename','elocation']
admin.site.register(Department,DepartmentAdmin)    
class RoleAdmin(admin.ModelAdmin) :
    list_display=['eno','ename']  
admin.site.register(Role,RoleAdmin)     
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','efirst_name','elast_name','esal','ebonus','ephone','ehire_date']
     
admin.site.register(Employee,EmployeeAdmin)

