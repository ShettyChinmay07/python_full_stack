
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Studentform_data
from .models import Student_table


def home(request):
    data1 = {
        'name': "Pratiksha",
        'age': 19,
        'department': "BCA"
    }

    marks = [100, 99, 98]

    return render(request, 'home.html', {
        'data1': data1,
        'marks1': marks
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def forms1(request):
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        email = request.POST.get('email')

        Student_table.objects.create(
            reg_no=reg_no,
            name=name,
            email=email,
            marks=marks
        )

        return HttpResponse("Saved successfully!!")

    return render(request, 'studentform.html')


def student_form_dj(request):
    if request.method == "POST":
        form = Studentform_data(request.POST)

        if form.is_valid():
            return HttpResponse("Saved successfully!!")

        else:
            return render(request, 'student_form_data.html', {
                'form': form
            })

    else:
        form = Studentform_data()

    return render(request, 'studentformdata.html', {'form': form})
    
