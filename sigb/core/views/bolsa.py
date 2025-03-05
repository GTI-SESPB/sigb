from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, UpdateView

from ..forms.bolsa import BolsaForm
from ..models.bolsa import Bolsa
from ..models.bolsista import Bolsista


__all__ = [
    'BolsaCreate',
    'BolsaUpdate',
]


class BolsaCreate(LoginRequiredMixin, View):
    template_name =  'core/bolsa_form.html'

    def get(self, request, bolsista_id):
        form = BolsaForm()
        bolsista = Bolsista.objects.get(pk=bolsista_id)
        form.fields['edital'].queryset = bolsista.edital_set.all()

        return render(request, self.template_name, { 'form': form })

    def post(self, request, bolsista_id):
        form = BolsaForm(request.POST)

        if form.is_valid():
            form.instance.bolsista_id = bolsista_id
            form.save()
            return redirect('bolsista_detail', pk=bolsista_id)

        return render(request, self.template_name, { 'form': form })


class BolsaUpdate(LoginRequiredMixin, View):
    template_name =  'core/bolsa_form.html'

    def get(self, request, pk):
        bolsa = Bolsa.objects.get(pk=pk)
        form = BolsaForm(instance=bolsa)
        bolsista = Bolsista.objects.get(pk=bolsa.bolsista_id)
        form.fields['edital'].queryset = bolsista.edital_set.all()

        return render(request, self.template_name, { 'form': form })

    def post(self, request, pk):
        bolsa = Bolsa.objects.get(pk=pk)
        form = BolsaForm(request.POST, instance=bolsa)

        if form.is_valid():
            form.save()
            return redirect('bolsista_detail', pk=bolsa.bolsista_id)

        return render(request, self.template_name, { 'form': form })
