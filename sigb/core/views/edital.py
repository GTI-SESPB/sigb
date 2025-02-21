from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView

from ..forms import EditalForm
from ..models import Edital


class EditalList(LoginRequiredMixin, ListView):
    model = Edital
    paginate_by = 25
    template_name = 'edital/list.html'

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
    template_name = 'edital/create.html'
    success_url = '/edital/list'


class EditalUpdate(LoginRequiredMixin, UpdateView):
    model = Edital
    form_class = EditalForm
    template_name = 'edital/update.html'
    success_url = '/edital/list'
