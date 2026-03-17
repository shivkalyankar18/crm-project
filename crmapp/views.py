from django.shortcuts import render, redirect
from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm
from django.contrib import messages, auth
from .models import Record
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,template_name='home.html')

# -Register a User

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')

    context = {'form':form}
    return render(request,template_name='register.html',context=context)



def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(request,username=username, password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request,'User logged in successfully')
                return redirect('dashboard')

    context = {'form':form}
    return render(request,template_name='login.html',context=context)


@login_required(login_url='login/')
def dashboard(request):
    records = Record.objects.all()
    context = {'records':records}
    return render(request,template_name='dashboard.html',context=context)

# Create Record

def create_record(request):
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Record created successfully')
            return redirect('dashboard')

    context = {'form':form}
    return render(request,template_name='create-record.html',context=context)

# Update Record

@login_required(login_url='login')
def update_record(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request,'Record updated successfully')
            return redirect('dashboard')

    context = {'form':form}
    return render(request,template_name='update-record.html',context=context)


# Delete Record

@login_required(login_url='login')
def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,'Record deleted successfully')

    return redirect('dashboard')

# Read/View Single Record
@login_required(login_url='login')
def singular_record(request,pk):
    record = Record.objects.get(id=pk)

    context = {'record':record}

    return render(request,template_name='view-record.html',context=context)


# User Logout

def user_logout(request):
    auth.logout(request)
    messages.success(request,'User logged out successfully')
    return redirect('login')
