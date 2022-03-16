from django.shortcuts import render
from django.views.generic import ListView
# from django.con import loginview
# from .models import Aemloyee
# Create your views here.


# class AddEmployee(ListView):
#     # model = 
    # template_name = 'templatemo_572_designer/index.html/'



def homepage(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'about.html')
    

def contact(request):
    return render(request,'contact.html')


def trend(request):
    return render(request,'trending.html')
    
def explore(request):
    return render(request,'explore.html') 

# class EmployeeRegister():
    
# class RegisterView()



