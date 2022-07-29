from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from apps.usuarios.forms import FormUser,FormLogin

# Create your views here.
class Login(FormView):
    template_name = 'accounts/login.html'
    form_class = FormLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class Register(CreateView):
    template_name = 'accounts/register.html'
    form_class = FormUser
    success_url = reverse_lazy('login')

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse(status = 204)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
