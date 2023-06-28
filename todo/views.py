from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoForm
from datetime import datetime


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        print(form)
        if form.is_valid():
            TodoList.objects.create(title=form.cleaned_data.get('title'), description=form.cleaned_data.get('description'))
            #form.save() above line or this line
            return redirect('home')
        
    return render(request, 'todo/home.html', {
        'title': 'Home',
        'todo_lists': TodoList.objects.all(),
        'form': TodoForm(request.POST),
    })


def update(request, id):
    obj = get_object_or_404(TodoList, pk=id)

    if request.method == 'POST':
        # form = TodoForm(request.POST) or
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            obj.modified_date = datetime.now()
            form.save() 
            ''' or
            for item in form.cleaned_data.keys():
                if item=='title':
                    obj.title = form.cleaned_data[item]
                elif item=='description':
                    obj.description = form.cleaned_data[item]
            obj.save()
            '''
            return redirect('home')

    return render(request, 'todo/update.html', {
        'form': TodoForm(instance=obj),
    })

def delete(request, id):
    obj = get_object_or_404(TodoList, pk=id)
    obj.delete()
    return redirect('home')