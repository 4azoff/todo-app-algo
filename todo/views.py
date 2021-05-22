from todo.models import Todo
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    if request.method == "POST":
        new_todo= Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request, 'index.html', {'todos':todos})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("/")