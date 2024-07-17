from django import forms
from . models import BatchMaster
from . models import StudentMaster
from . models import PaperMaster
from . models import SemMaster
from . models import CourseMaster
from . models import ExamMaster
from . models import *

class BatchForm(forms.ModelForm):
    class Meta:
        model=BatchMaster
        fields="__all__"
class BatchMasterForm(forms.Form):
    query = forms.CharField(label='Batch_no', max_length=100)


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentMaster
        fields="__all__"
class PaperForm(forms.ModelForm):
    class Meta:
        model=PaperMaster
        fields="__all__"
class PaperMasterForm(forms.Form):
    query = forms.CharField(label='PaperCode', max_length=100)
class SemForm(forms.ModelForm):
    class Meta:
        model=SemMaster
        fields="__all__"
class SemMasterForm(forms.Form):
    query = forms.CharField(label='Semester', max_length=100)
class CourseForm(forms.ModelForm):
    class Meta:
        model=CourseMaster
        fields="__all__"
class CourseMasterForm(forms.Form):
    query = forms.CharField(label='Course', max_length=100)

class ExamForm(forms.ModelForm):
    class Meta:
        model=ExamMaster
        fields="__all__"
class ExamMasterForm(forms.Form):
    query = forms.CharField(label='Exam_type', max_length=100)
class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeModel
        fields='__all__'
    def clean(self):
        super(EmployeeForm,self).clean()
        first_name=self.cleaned_data.get('first_name')
        last_name=self.cleaned_data.get('last_name')
        mobile=self.cleaned_data.get('mobile')
        email=self.cleaned_data.get('email')
        if len(first_name)<3:
            self._errors['first_name']=self.error_class(['A Minimum of 5 characters is required'])
        for i in first_name:
            if i not in 'ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz':
                self._errors['first_name']=self.error_class(['First name should contain 5 characters is required'])
        if len(mobile)!=10:
            self._errors['mobile']=self.error_class(['Mobile number length should have 10 digits'])
        for i in mobile:
            if i not in  '0123456789':
                self._errors['mobile']=self.error_class(['Mobile number  should have contain digits'])
        return self.cleaned_data
class EmployeeSearchForm(forms.Form):
    query = forms.CharField(label='FIRST_NAME', max_length=100)


