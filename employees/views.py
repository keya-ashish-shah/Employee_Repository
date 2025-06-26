from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse
from employees.models import Employee

# Create your views here.
def employee_detail(request,pk):
    # try:
    #     employee=Employee.objects.get(pk=pk)
    #     print(employee)
    # except:
    #     raise Http404
    employee = get_object_or_404(Employee,pk=pk)
    # print(employee) prints in console only therefore using below res method 
    # return HttpResponse(employee)
    context = {
        'employee': employee,
    }
    return render(request,'employee_detail.html',context)