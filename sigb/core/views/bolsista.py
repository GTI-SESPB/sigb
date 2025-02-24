from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .utils import DownloadView
from ..forms import BolsistaForm, BolsistaBolsaForm
from ..models import Bolsista, BolsistaBolsa


__all__ = [
    'BolsistaList',
    'BolsistaDetailView',
    'BolsistaCreate',
    'BolsistaUpdate',
    'BolsistaDownload',
    'AdicionarBolsaBolsista',
    'AtualizarBolsaBolsista',
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bolsas = BolsistaBolsa.objects.filter(bolsista=self.object.id)
        context.update({ 'bolsas': bolsas })

        return context


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
    template_name = 'bolsista/adicionar_bolsa/form.html'

    def get(self, request, bolsista_id, **kwargs):
        bolsista = get_object_or_404(Bolsista, pk=int(bolsista_id))
        return render(request, self.template_name, {
            'form': kwargs.get('form', BolsistaBolsaForm), 'bolsista': bolsista 
        })

    def post(self, request, bolsista_id):
        form = BolsistaBolsaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('bolsista_detail', pk=bolsista_id)

        return self.get(request, bolsista_id, form=form)


class AtualizarBolsaBolsista(LoginRequiredMixin, View):
    template_name = 'bolsista/adicionar_bolsa/form.html'

    def get(self, request, bolsista_id, pk, **kwargs):
        vinculo = BolsistaBolsa.objects.get(id=int(pk))
        initial = {
            'vigencia_outorga': vinculo.vigencia_outorga.strftime('%Y-%m-%d'),
            'data_outorga': vinculo.data_outorga.strftime('%Y-%m-%d'),
        }
        if vinculo.dt_desligamento:
            initial['dt_desligamento'] = vinculo.dt_desligamento.strftime('%Y-%m-%d'),

        bolsista = get_object_or_404(Bolsista, pk=int(bolsista_id))
        if form := kwargs.get('form') is None:
            form = BolsistaBolsaForm(
                initial=initial,
                instance=vinculo
            )

        return render(
            request,
            self.template_name,
            { 'form': form, 'bolsista': bolsista, 'vinculo': vinculo }
        )

    def post(self, request, bolsista_id, pk):
        vinculo = BolsistaBolsa.objects.get(id=int(pk))
        form = BolsistaBolsaForm(request.POST, request.FILES, instance=vinculo)
        if form.is_valid():
            form.save()
            return redirect('bolsista_detail', pk=bolsista_id)

        return self.get(request, bolsista_id, pk, form=form)
