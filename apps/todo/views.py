from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,View,UpdateView
from django.urls import reverse_lazy
import json
from apps.todo import models 
from apps.todo import forms
# Create your views here.

class Todo(View):
    model = models.ToDo
    template_name = 'todo.html'
    #success_url = reverse_lazy('index')
    #form_class = forms.formTodo

    def post(self,request):
        user = request.user
        content = request.POST.get('content')
        if content:
            task = self.model.objects.create(
            #user = user,
            content = request.POST.get('content'),
            status = 0
        )
        task.save()
        success = {
            'task':task.content,
            'status':task.get_status_display(),
            'id':task.id
        }
        print(success)
        return redirect(request.path)
        return JsonResponse(success)
            
    def get(self,request):
        progress = self.model.objects.filter(status = 0).order_by('-id')
        context = {
            'progress':progress
        }
        return render(request,self.template_name,context)

class DeleteTodo(UpdateView):
    model = models.ToDo
    template_name = 'tasks/delete_tasks.html'
    def get(self,request,pk):
        task = self.model.objects.get(id = pk)
        context = {
            'task':task
        }
        return render(request,self.template_name,context)
        
    def post(self,request,pk):
        todo = self.model.objects.get(id = pk)
        todo.delete()
        return HttpResponse(status = 204)

class EndTask(UpdateView):
    model = models.ToDo
    def post(self,request,pk):
        task = self.model.objects.get(id = pk)
        if task:
            task.status = 1
            task.save()
        return HttpResponse(status = 204)

class FinishedTask(View):
    model = models.ToDo
    template_name = 'tasks/finished_tasks.html'
    success_url = reverse_lazy('index')
    def get(self,request):
        user = request.user
        tasks = self.model.objects.filter(status = 1)
        context = {
            'tasks':tasks
        }
        return render(request,self.template_name,context)