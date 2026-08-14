from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import TaskForm
from .models import Task


def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("garden:home")
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    completed = tasks.filter(completed=True)
    total = tasks.count()
    progress = round((completed.count() / total) * 100) if total else 0
    return render(request, "garden/home.html", {
        "form": form, "tasks": tasks, "flowers": completed,
        "progress": progress, "total": total,
    })


def toggle_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id)
        task.completed = not task.completed
        task.completed_at = timezone.now() if task.completed else None
        task.save()
    return redirect("garden:home")


def delete_task(request, task_id):
    if request.method == "POST":
        get_object_or_404(Task, pk=task_id).delete()
    return redirect("garden:home")
