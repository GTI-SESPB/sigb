from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView

from ..forms import BolsaForm
from ..models import Bolsa


__all__ = [
    'BolsaList',
    'BolsaCreate',
    'BolsaUpdate',
]


class BolsaList(LoginRequiredMixin, ListView):
    model = Bolsa
    paginate_by = 25
    template_name = 'bolsa/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get(self.page_kwarg) or 1
        page_range = context['paginator'].get_elided_page_range(
            number=page, on_each_side=2, on_ends=1
        )
        context.update({ 'page_range': page_range })

        return context


class BolsaCreate(LoginRequiredMixin, CreateView):
    model = Bolsa
    form_class = BolsaForm
    template_name = 'bolsa/create.html'
    success_url = '/bolsista/list'


class BolsaUpdate(LoginRequiredMixin, UpdateView):
    model = Bolsa
    form_class = BolsaForm
    template_name = 'bolsa/update.html'
    success_url = '/bolsa/list'
