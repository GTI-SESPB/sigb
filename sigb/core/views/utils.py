import csv

from django.db import models
from django.http import StreamingHttpResponse
from django.views.generic import View


class DownloadView(View):
    model: models.Model

    @classmethod
    def csv_gerador(cls, writer, queryset):
        field_names = [
            field.name 
            for field 
            in cls.model._meta.fields
        ]
        yield writer.writerow(field_names)

        for obj in queryset.iterator():
            yield writer.writerow([
                getattr(obj, field) for field in field_names
            ])

    def get(self, _):
        queryset = self.model.objects.all()
        buffer = self.Echo()
        writer = csv.writer(buffer)
        return StreamingHttpResponse(
            self.csv_gerador(writer, queryset),
            content_type='text/csv',
            headers={
                "Content-Disposition": 'attachment; filename="bolsistas_exportacao.csv"'
            }
        )

    class Echo:
        def write(self, value):
            return value
