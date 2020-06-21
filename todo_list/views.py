from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo_list.models import Tasklist
from todo_list.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required   #used to page restriction(only logged in user can view the page)
def todolist(request):
    if request.method=="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user      #to add user (manager) name
            instance.save()
        messages.success(request,('New Task added!'))
        return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.filter(manage=request.user)    # to show only that task which are added by particular user
        paginator = Paginator(all_tasks, 2)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks':all_tasks})

@login_required
def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()


        messages.success(request, ('Task Edited'))
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)

        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')




def index(request):
    context ={
        'index_text': "Welcome to Index Page"
        }
    return render(request, 'index.html', context)


def contact(request):
    context ={
        'contact_text': "Welcome to contact page"
        }
    return render(request, 'contact.html', context)

def about(request):
    context ={
        'about_text': "Welcome to about"
        }
    return render(request, 'about.html', context)

