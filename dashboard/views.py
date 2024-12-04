from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from list.models import Todo
# Create your views here.
@login_required
def index(request):
    todos = Todo.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'todos': todos,
    })


