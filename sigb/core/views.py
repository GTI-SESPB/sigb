from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import render, redirect

from .forms import BolsistaForm
from .models import Bolsista

# Create your views here.

def home(_):
    return redirect('bolsista_list')


class BolsistaList(LoginRequiredMixin, ListView):
    model = Bolsista
    paginate_by = 25
    template_name = 'bolsista/list.html'

    def get_context_data(self):
        context = super().get_context_data()
        page = self.request.GET.get(self.page_kwarg) or 1
        page_range = context['paginator'].get_elided_page_range(
            number=page, on_each_side=2, on_ends=1
        )
        context.update({ 'page_range': page_range })

        return context


class BolsistaUpdate(LoginRequiredMixin, UpdateView):
    model = Bolsista
    form_class = BolsistaForm
    template_name = 'form.html'
    success_url = '/bolsista/list'


class BolsistaCreate(LoginRequiredMixin, CreateView):
    model = Bolsista
    form_class = BolsistaForm
    template_name = 'form.html'
    success_url = '/bolsista/list'
