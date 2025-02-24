from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View
from django.shortcuts import render, redirect, reverse

from .utils import DownloadView
from ..forms import BolsistaForm, BolsistaBolsaForm
from ..models import Bolsista


__all__ = [
    'BolsistaList',
    'BolsistaDetailView',
    'BolsistaCreate',
    'BolsistaUpdate',
    'BolsistaDownload',
    'AdicionarBolsaBolsista',
]


class BolsistaList(LoginRequiredMixin, ListView):
    model = Bolsista
    paginate_by = 25
    template_name = 'bolsista/list.html'
    context_object_name = 'bolsistas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get(self.page_kwarg) or 1
        page_range = context['paginator'].get_elided_page_range(
            number=page, on_each_side=2, on_ends=1
        )
        context.update({ 'page_range': page_range })

        return context


class BolsistaDetailView(LoginRequiredMixin, DetailView):
    model = Bolsista
    template_name = 'bolsista/detail.html'


class BolsistaCreate(LoginRequiredMixin, CreateView):
    model = Bolsista
    form_class = BolsistaForm
    template_name = 'bolsista/create.html'

    def get_success_url(self):
        return reverse('bolsista_detail', kwargs={ 'pk': self.object.id })


class BolsistaUpdate(LoginRequiredMixin, UpdateView):
    model = Bolsista
    form_class = BolsistaForm
    template_name = 'bolsista/update.html'

    def get_object(self):
        obj = super().get_object()
        obj.dt_nascimento = obj.dt_nascimento.strftime('%Y-%m-%d')
        return obj

    def get_success_url(self):
        return reverse('bolsista_detail', kwargs={ 'pk': self.object.id })


class BolsistaDownload(LoginRequiredMixin, DownloadView):
    model = Bolsista


class AdicionarBolsaBolsista(LoginRequiredMixin, View):
    template_name = 'bolsa/vinculo_bolsista_create.html'

    def get(self, request, **_):
        return render(request, self.template_name, { 'form': BolsistaBolsaForm })

    def post(self, request, pk):
        form = BolsistaBolsaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('bolsista_update', pk=pk)

        return render(request, self.template_name, { 'form': form })
