from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from ..forms.edital import EditalForm, EditalVincularBolsistaForm
from ..models.bolsista import Bolsista
from ..models.edital import Edital


__all__ = [
    'EditalList',
    'EditalCreate',
    'EditalUpdate',
    'EditalVincularBolsistaView',
]


class EditalList(LoginRequiredMixin, ListView):
    model = Edital
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get(self.page_kwarg) or 1
        page_range = context['paginator'].get_elided_page_range(
            number=page, on_each_side=2, on_ends=1
        )
        context.update({ 'page_range': page_range })

        return context


class EditalCreate(LoginRequiredMixin, CreateView):
    model = Edital
    form_class = EditalForm
    success_url = reverse_lazy('edital_list')


class EditalUpdate(LoginRequiredMixin, UpdateView):
    model = Edital
    form_class = EditalForm
    success_url = reverse_lazy('edital_list')
    template_name_suffix = '_update_form'


class EditalVincularBolsistaView(LoginRequiredMixin, View):
    template_name = 'core/edital_vincular_bolsista_form.html'

    def get(self, request, **_):
        form = EditalVincularBolsistaForm()
        return render(request, self.template_name, { 'form': form })

    def post(self, request, bolsista_id):
        form = EditalVincularBolsistaForm(request.POST)

        if form.is_valid():
            bolsista = Bolsista.objects.get(pk=bolsista_id)
            edital = form.cleaned_data['edital']
            edital.bolsistas.add(bolsista)

        return self.get(request)
