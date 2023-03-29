from django.forms import ModelForm
from .models import *
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'status','roll','reg_no','description','dept','dob','name','fathers_name','mothers_name','session','hsc_roll','hsc_reg','CGPA','result_description']


class StudentFormForPendingStd(ModelForm):
    class Meta:
        model = Student
        fields='__all__'
        exclude = ['user','status','description','CGPA','result_description']
 


class DeptFormForPendingDept(ModelForm):
    class Meta:
        model = Department
        fields='__all__'
        exclude = ['user','status','rank']



class StudentFormAdmin(ModelForm):
    class Meta:
        model = Student
        fields='__all__'
        exclude=['user','CGPA','result_description']




class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        exclude = ['user']



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class TeacherForm(forms.ModelForm):
    class Meta:
        
        model = Teacher
        fields = '__all__'




class StudentResultForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['CGPA', 'result_description']
        widgets = {
            'CGPA': forms.NumberInput(attrs={'min': 0.0, 'max': 4.0, 'class': 'form-control'}),
            'result_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 17}),
        }
        labels = {
            'CGPA': 'CGPA (out of 4.0)',
            'result_description': 'Result Description',
        }





class AdminNoticeForm(forms.ModelForm):
    class Meta:
        
        model = AdminNotice
        fields = '__all__'