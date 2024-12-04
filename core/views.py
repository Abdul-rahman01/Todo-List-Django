from django.shortcuts import render, redirect
from list.models import Todo
from .forms import SignupForm
from django.contrib.auth import logout

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'core/index.html', {
        'todos': todos,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('/')