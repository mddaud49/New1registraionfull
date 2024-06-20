from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render (request,'home.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def register(request):
    return render (request,'register.html')

# def dashboard(request):
#     return render (request,'dashboard.html')
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})

def login(request):
    return render (request,'login.html')

def logindata(request):
    # print(request.POST)
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=Student.objects.filter(Email=email)
    if user:
        data=Student.objects.get(Email=email)
        if data.Password==password:
            print("Matched password")
            name=data.Name
            email=data.Email
            password=data.Password
            contact=data.Contact
            user={
                'name':name,
                'email':email,
                'contact':contact,
                'password':password,
            }
            return render(request,'dashboard.html',user)
            
        else:
            msg="password does not match"
            return render(request,'login.html',{'msg':msg})
    else:
        msg="user does not exit"
        return render(request,'register.html',{'msg':msg})
    return render(request,'login.html',{'msg':msg})



def registerdata(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('pass')
    cpassword=request.POST.get('cpassword')
    data=Student.objects.filter(Email=email)
    if data:
        msg="user already exit"
        return render(request,'register.html',{'key':msg})
    else:
        if password==cpassword:
            Student.objects.create(Name=name,
                                   Contact=contact,
                                   Email=email,
                                   Password=password)
            msg="registration successfully"
            return render(request,'login.html',{'key':msg})
        else:
            msg="password &cpassword not matched"
            return render(request,'register.html',{'key':msg})
        

def logout(request):
    return render (request,'home.html')

