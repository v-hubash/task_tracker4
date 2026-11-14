from django.shortcuts import render
from .models import Task, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    
