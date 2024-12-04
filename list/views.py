from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewTodoForm, EditTodoForm
from .models import Todo

# Create your views here.
@login_required
def new(request):
    if request.method == 'POST':
        form = NewTodoForm(request.POST,)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_by = request.user
            todo.save()

            return redirect('dashboard:index')
    
    else:
        form = NewTodoForm()

    return render(request, 'list/form.html', {
        'form': form,
        'title': 'New todo',
    })


@login_required
def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        form = EditTodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()

            return redirect('dashboard:index')
    
    else:
        form = EditTodoForm(instance=todo)

    return render(request, 'list/form.html', {
        'form': form,
        'title': 'Edit todo',
    })


@login_required
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()

    return redirect('dashboard:index')