from django import forms
from . import models

class CreateStudentForm(forms.ModelForm):
    
    class Meta:
        model = models.Student
        fields = ['fname', 'sname', 'mname', 'email','mobile','department','level','matric','address', 'password']


