from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee
#simple send 
# def home(request):
#     return HttpResponse("hello world")

#html render simple
# def home(request):
#     return render(request , 'home.html')

# return data from db to html via html render method 
def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request , 'home.html', context)