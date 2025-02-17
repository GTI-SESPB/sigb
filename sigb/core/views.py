import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import StreamingHttpResponse
from django.views.generic import CreateView, ListView, UpdateView, View
from django.shortcuts import render, redirect

from .forms import BolsistaForm, BolsaForm, EditalForm, RelacaoBolsistaBolsaForm
from .models import Bolsista, Bolsa, Edital, RelacaoBolistaBolsa


def home(_):
    return redirect('bolsista_list')


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

class Echo:
    def write(self, value):
        return value

class BolsistaCreate(LoginRequiredMixin, CreateView):
    model = Bolsista
    form_class = BolsistaForm
    template_name = 'bolsista/create.html'
    success_url = '/bolsista/list'


class BolsistaUpdate(LoginRequiredMixin, UpdateView):
    model = Bolsista
    form_class = BolsistaForm
    template_name = 'bolsista/update.html'
    success_url = '/bolsista/list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bolsista_pk = self.kwargs.get(self.pk_url_kwarg)
        bolsista = Bolsista.objects.get(id=bolsista_pk)
        bolsas = RelacaoBolistaBolsa.objects.filter(bolsista=bolsista)

        context.update({
            'bolsista': bolsista,
            'bolsas': bolsas
        })

        return context


class BolsistaDownload(LoginRequiredMixin, View):

    @staticmethod
    def csv_gerador(writer, queryset):
        field_names = [
            field.name 
            for field 
            in Bolsista._meta.fields
        ]
        yield writer.writerow(field_names)

        for obj in queryset.iterator():
            yield writer.writerow([
                getattr(obj, field) for field in field_names
            ])

    def get(self, _):
        queryset = Bolsista.objects.all()
        buffer = Echo()
        writer = csv.writer(buffer)
        return StreamingHttpResponse(
            self.csv_gerador(writer, queryset),
            content_type='text/csv',
            headers={
                "Content-Disposition": 'attachment; filename="bolsistas_exportacao.csv"'
            }
        )


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


class VinculoBolsaBolsistaCreate(LoginRequiredMixin, View):
    template_name = 'bolsa/vinculo_bolsista_create.html'

    def get(self, request, **_):
        return render(request, self.template_name, { 'form': RelacaoBolsistaBolsaForm })

    def post(self, request, pk):
        form = RelacaoBolsistaBolsaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('bolsista_update', pk=pk)

        return render(request, self.template_name, { 'form': form })
