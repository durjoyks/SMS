from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group





def registerstd(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form= CreateUserForm()


        if request.method=='POST':
                form=CreateUserForm(request.POST)
                if form.is_valid():
                    user=form.save()
                    username=form.cleaned_data.get('username')
                    group=Group.objects.get(name='student')
                    user.groups.add(group)
                    Student.objects.create(
                        user=user,
                    )
                    messages.success(request,'Account Created ' +username)
                    return redirect('login')
    

    context={'form':form}
    return render(request,'app1/register.html',context)




@unauthenticated_user
def loginstd(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect') 

    return render(request,'app1/login.html')





def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    top_5_dept=Department.objects.filter(rank__lt=6).order_by('rank')
    all_dept=Department.objects.all()
    all_std=Student.objects.all().order_by('-id')[:5]
    all_teacher=Teacher.objects.all()
    total_teacher=all_teacher.count()
    total_std=all_std.count()
    total_dept=all_dept.count()
    context={'top_5_dept':top_5_dept,'all_dept':all_dept,'total_dept':total_dept,'all_std':all_std,'total_std':total_std,'total_teacher':total_teacher,'all_teacher':all_teacher}
    return render( request,'app1/home.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userPage(request):
    try:
        student = request.user.student
    except Student.DoesNotExist:
        student = None
    context={'student':student}
    return render(request,'app1/user.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def accountSettings(request):
    student=request.user.student
    form = StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES,instance=student)
        if form.errors:
           print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('user-page')

    context={'form':form,'student':student}
    return render(request, 'app1/account_settings.html',context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def accountSettingsPendingStd(request):
    student=request.user.student
    
    form = StudentFormForPendingStd(instance=student)
    if request.method=='POST':
        form=StudentFormForPendingStd(request.POST,request.FILES,instance=student)
        if form.errors:
            print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('user-page')


    context={'form':form,'student':student}
    return render(request, 'app1/acc_set_pen_std.html',context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def department(request,pk):
    dept=Department.objects.get(id=pk)
    teachers=dept.teacher_set.all()
    students=dept.student_set.filter(status='Accecpted').order_by('-id')
    total_teacher=teachers.count()
    total_student=students.count()
    context={'dept':dept,'teachers':teachers,'total_teacher':total_teacher,'students':students,'total_student':total_student}
    return render(request,'app1/department.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','department'])
def studentinfo(request,pk):
    student=Student.objects.get(id=pk)
    context={'student':student}
    return render(request,'app1/studentinfo.html',context)
    


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def nav_stu(request):

    students=Student.objects.filter(status='Accecpted').order_by('-id')
    total_std=students.count()
    context={'students':students,'total_std':total_std,'title': 'Students'}
    return render(request,'app1/nav_stu.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def nav_dept(request):

    depts=Department.objects.filter(status='Accecpted')
    total_dept=depts.count()

    departments=Department.objects.filter(status='Pending').order_by('id')
    dr=departments.count()

    myFilter=DepartmentFilter(request.GET, queryset=depts)
    depts=myFilter.qs
    
    context={'depts':depts,'total_dept':total_dept,'myFilter':myFilter,'departments':departments,'dr':dr}
    return render(request,'app1/nav_dept.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_dept(request):
    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            rank = form.cleaned_data['rank']
            if Department.objects.filter(rank=rank).exists():
                messages.info(request,'Already exists a dept with this Rank')
            else:
                form.save()
                return redirect('/')
    context = {'form':form}
    return render(request,'app1/dept_form.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_dept(request,pk):
    item = Department.objects.get(id=pk)
    form = DepartmentForm(instance=item)
    current_rank=item.rank

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=item)
        if form.is_valid():
            rank = form.cleaned_data['rank']
            if rank != current_rank and Department.objects.filter(rank=rank).exists():
                messages.info(request,'Already exists a dept with this Rank')
            else:
                form.save()
                return redirect('/')

    context = {'form':form}
    return render(request,'app1/dept_form.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_dept(request,pk):
    item=Department.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context={'item':item,'func':'delete_dept'}
    return render(request,'app1/delete.html',context)



def create_std(request):
     
    form = StudentFormAdmin()

    if request.method == 'POST':
        form=StudentFormAdmin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'app1/std_form.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_std(request,pk):
    item=Student.objects.get(id=pk)
    form =StudentFormAdmin(instance=item)

    if request.method == 'POST':
        form=StudentFormAdmin(request.POST,instance=item)
        if form.errors:
           print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'app1/std_form.html',context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_std(request,pk):
    item=Student.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context={'item':item,'func':'delete_std'}
    return render(request,'app1/delete.html',context)




@allowed_users(allowed_roles=['admin'])
def accept_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.status = 'Accecpted'
    student.save()
    return redirect('nav_stu')




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Request(request):

    students=Student.objects.filter(status='Pending').order_by('id')
    total_std=students.count()

    context={'students':students,'total_std':total_std,'title': 'Student Requests','func':'std_req'}
    return render(request,'app1/nav_stu.html',context)
     



def register_dpt(request) :

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form= CreateUserForm()

    if request.method=='POST':
                form=CreateUserForm(request.POST)
                if form.is_valid():
                    user=form.save()
                    username=form.cleaned_data.get('username')
                    group=Group.objects.get(name='department')
                    user.groups.add(group)
                    Department.objects.create(
                        user=user,
                    )
                    messages.success(request,'Account Created ' +username)
                    return redirect('login')
    context={'form':form}
    return render(request,'app1/register_dpt.html',context)




@allowed_users(allowed_roles=['department'])
def deptPage(request):
    dept=request.user.department
    teachers=dept.teacher_set.all()
    students=dept.student_set.filter(status='Accecpted').order_by('-id')
    total_teacher=teachers.count()
    total_student=students.count()
    context={'dept':dept,'teachers':teachers,'total_teacher':total_teacher,'students':students,'total_student':total_student}
    return render(request,'app1/deptpage.html',context)



@allowed_users(allowed_roles=['department'])
def acc_set_dept_pen(request):
    department=request.user.department
    dept=department   
    form = DeptFormForPendingDept(instance=department)
    if request.method=='POST':
        form=DeptFormForPendingDept(request.POST,request.FILES,instance=department)
        if form.errors:
            print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('dept-page')

    context={'form':form,'dept':dept}
    return render(request, 'app1/acc_set_dept_pen.html',context)



@allowed_users(allowed_roles=['admin'])
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'app1/create_teacher.html', {'form': form})




@allowed_users(allowed_roles=['admin'])
def teacher_list(request):
    teachers=Teacher.objects.all()
    total_teacher=teachers.count()
    context={'teachers':teachers,'total_teacher':total_teacher}
    return render(request, 'app1/teacher_list.html',context)



@allowed_users(allowed_roles=['admin'])
def teacher_info(request,pk):
    teacher=Teacher.objects.get(id=pk)
    context={'teacher':teacher}
    return render(request, 'app1/teacher_info.html',context)


@allowed_users(allowed_roles=['admin'])
@allowed_users(allowed_roles=['admin'])
def delete_teacher(request, pk):
    teacher =Teacher.objects.get(id=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'app1/teacher_info.html')



@allowed_users(allowed_roles=['admin','department','student'])
def result_details(request, pk):
    student =Student.objects.get(id=pk)
    context={'student':student}      
    return render(request,'app1/result.html',context)


@allowed_users(allowed_roles=['admin'])
def update_student_result(request, pk):
    student = Student.objects.get(id=pk)
    last_page_url = request.META.get('HTTP_REFERER')
    form = StudentResultForm(instance=student)
    if request.method == 'POST':
        form = StudentResultForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            if not last_page_url or last_page_url == request.build_absolute_uri():
               return redirect('nav_stu')
    context = {'form': form}
    return render(request, 'app1/update_result.html', context)





def admin_send_notice(request):
    if request.method == 'POST':
        form = AdminNoticeForm(request.POST)
        if form.is_valid():  
           notice = form.save()
           return redirect('home')
    else:
       form = AdminNoticeForm()

    return render(request, 'app1/admin_send_notice.html', {'form': form})


def admin_notice_list(request):
    notices = AdminNotice.objects.all()
    context = {'notices': notices}  # use parentheses instead of curly braces
    return render(request, 'app1/admin_notice_list.html', context)
