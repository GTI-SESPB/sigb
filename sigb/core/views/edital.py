from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from ..forms.edital import EditalForm
from ..models.edital import Edital


__all__ = [
    'EditalList',
    'EditalCreate',
    'EditalUpdate',
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

    def get_success_url(self):
        return reverse('edital_list')


class EditalUpdate(LoginRequiredMixin, UpdateView):
    model = Edital
    form_class = EditalForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('edital_list')
