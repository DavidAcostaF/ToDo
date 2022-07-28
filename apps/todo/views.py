from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,View,UpdateView
from django.urls import reverse_lazy

from apps.todo import models 
from apps.todo import forms
# Create your views here.

class Todo(View):
    model = models.ToDo
    template_name = 'todo.html'
    success_url = reverse_lazy('index')
    #form_class = forms.formTodo

    def post(self,request):
        user = request.user
        content = request.POST.get('content')
        print(type(content))
        if content:
            self.model.objects.create(
            #user = user,
            content = request.POST.get('content'),
            status = 0
        )
        return HttpResponse(status = 204)
            
    def get(self,request):
        progress = self.model.objects.filter(status = 0)
        context = {
            'progress':progress
        }
        return render(request,self.template_name,context)

class DeleteTodo(UpdateView):
    model = models.ToDo
    def post(self,request,pk):
        print(pk)
        todo = self.model.objects.get(id = pk)
        todo.delete()
        return HttpResponse(status = 204)