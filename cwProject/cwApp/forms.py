from django import forms


# create form
class EmployeeForm(forms.Form):
    name = forms.CharField()
    dateOfBirth = forms.DateField()
    position = forms.CharField()
    salary = forms.IntegerField()
