from django.shortcuts import render,redirect
from .forms import TodoForm
from . models import Todo

def index(request):
    form=TodoForm()
    todo=Todo.objects.all()
    context={
        "form":form,
        "todo":todo
    }
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form. is_valid():
            form.save()
            return render(request,"index.html",context)
    return render(request,"index.html",context)
def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=='POST':
        todo.delete()
        return redirect("index")
    
def update(request,id):
    todo=Todo.objects.get(id=id)
    form=TodoForm(instance=todo)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request,"update.html",{"form":form})
    
    
