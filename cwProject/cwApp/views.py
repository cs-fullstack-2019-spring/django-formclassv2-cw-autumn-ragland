from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm


# access the form and render pages
def index(request):
    # if the form is being submitted render a submission html file with entered info
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'dob': request.POST['dateOfBirth'],
            'position': request.POST['position'],
            'salary': request.POST['salary']
        }
        return render(request, 'cwApp/submission.html', context)
    # if the form is being loaded render the form html file with the form created in the forms file
    else:
        newForm = EmployeeForm()
        context = {
            'newForm': newForm
        }
        return render(request, 'cwApp/index.html', context)
