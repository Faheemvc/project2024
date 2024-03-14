from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for student related form
class staffUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class staffForm(forms.ModelForm):
    class Meta:
        model=models.staff
        fields=['address','mobile','department','status','profile_pic']



#for teacher related form
class studentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class studentForm(forms.ModelForm):
    #this is the extrafield for linking student and their assigend staff
    #this will show dropdown __str__ method staff model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in staff model and return it
    assignedstaffId=forms.ModelChoiceField(queryset=models.staff.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.student
        fields=['address','mobile','status','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):
    staffId=forms.ModelChoiceField(queryset=models.staff.objects.all().filter(status=True),empty_label="staff", to_field_name="user_id")
    studentId=forms.ModelChoiceField(queryset=models.student.objects.all().filter(status=True),empty_label="student Name ", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status',]


class studentAppointmentForm(forms.ModelForm):
    staffId=forms.ModelChoiceField(queryset=models.staff.objects.all().filter(status=True),empty_label="Select staff", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status','date',]


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



