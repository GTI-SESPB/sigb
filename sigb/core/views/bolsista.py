from io import BytesIO

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import FileResponse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from reportlab.pdfgen import canvas

# from sigb.core.models.edital import Edital

from .utils import DownloadView
from ..forms.bolsista import BolsistaForm, BolsistaVincularEditalForm
from ..models.bolsista import Bolsista


__all__ = [
    'BolsistaList',
    'BolsistaDetailView',
    'BolsistaCreate',
    'BolsistaUpdate',
    'BolsistaDownload',
    'BolsistaVincularEditalView',
    # 'DeclaracaoVinculoView',
]


class BolsistaList(LoginRequiredMixin, ListView):
    model = Bolsista
    paginate_by = 25

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BolsistaCreate(LoginRequiredMixin, CreateView):
    model = Bolsista
    form_class = BolsistaForm

    def get_success_url(self):
        return reverse('bolsista_detail', kwargs={ 'pk': self.object.id })


class BolsistaUpdate(LoginRequiredMixin, UpdateView):
    model = Bolsista
    form_class = BolsistaForm
    template_name_suffix = '_update_form'

    def get_object(self):
        obj = super().get_object()
        obj.dt_nascimento = obj.dt_nascimento.strftime('%Y-%m-%d')
        return obj

    def get_success_url(self):
        return reverse('bolsista_detail', kwargs={ 'pk': self.object.id })


class BolsistaVincularEditalView(LoginRequiredMixin, View):
    template_name = 'core/bolsista_vincular_edital_form.html'

    def get(self, request, **_):
        form = BolsistaVincularEditalForm()
        return render(request, self.template_name, { 'form': form })

    def post(self, request, bolsista_id):
        form = BolsistaVincularEditalForm(request.POST)

        if form.is_valid():
            bolsista = Bolsista.objects.get(pk=bolsista_id)
            edital = form.cleaned_data['edital']

        return self.get(request)



class BolsistaDownload(LoginRequiredMixin, DownloadView):
    model = Bolsista


# class DeclaracaoVinculoView(LoginRequiredMixin, View):
#     def get(self, _, vinculo_id):
#         vinculo = BolsistaBolsa.objects.get(id=int(vinculo_id))
#
#         buffer = BytesIO()
#         pdf = canvas.Canvas(buffer)
#         pdf.drawString(250, 250, 'DECLARAÇÃO')
#         pdf.drawString(100, 750, '''
#         Declaro para todos devidos fins, que {nome}, inscrito no CPF n° {cpf},
#         é bolsista do Edital {edital} e exerce a atividade de {{atividade}},
#         vinculado ao Projeto {{projeto}}, desenvolvido pela Escola de Saúde Pública
#         da Paraíba - ESP/PB, entre {data_outorga} até o presente momento
#         '''.format(
#             nome=vinculo.bolsista.nome,
#             cpf=vinculo.bolsista.cpf,
#             edital=vinculo.edital,
#             data_outorga=vinculo.data_outorga
#         ))
#
#         pdf.showPage()
#         pdf.save()
#
#         buffer.seek(0)
#         return FileResponse(buffer, as_attachment=True, filename='declaracao.pdf')
