from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm


# Create your views here.

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('menu')
        return render(request, self.template_name, {'form': LoginForm})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['email'],
                password=form.cleaned_data['senha']
            )
            if user:
                login(request, user)

                if next_page:=request.GET.get('next'):
                    return redirect(next_page)

                return redirect('/') # TODO: alterar para página inicial

        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
