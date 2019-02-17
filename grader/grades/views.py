from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task
from grades.forms import classroom_create, task_create

from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def homepage(request):
    return render(request,"projects/main.html",{'msg':Classroom.objects.order_by('id')})

def classroom_create(request):
    if request.method == 'POST':
        cform = classroom_create(request.POST)
        if cform.is_valid():
            new_ classroom = cform.save(commit = False)
            new_classroom.owner = request.user
            new_classroom.save()
            return redirect('/main')
    else:
        cform = classroom_creating()
    return render(request,'projects/classroom_form.html',{"cform" : cform})

def classroom(request):
    if request.user.is_authenticated:
        return render(request,"projects/classroom.html",{'first_name':None})
    else:
        return render(request,"projects/classroom.html",{})

def classroom_deletion(request, project_number):
    project = get_object_or_404(classroom,id=project_number)
    context =  {"classroom" : classroom}
    if request.method == 'POST':
        project.delete()
        return redirect('/home')
    else:
        return render(request,'projects/delete_project.html',context)

def add_mark(request):
    if request.method == 'POST':
        aform = task_create((request.POST))
        if aform.is_valid():
            new_task = aform.save(commit = False)
            new_task.name = request.
            new_task.due_date = request.
            new_task.description = request.

def send_marks(marks):
    return render(request, 'templates/evidence_record.html', marks)

