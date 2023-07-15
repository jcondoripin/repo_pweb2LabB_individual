from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
import datetime
from relations.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, id):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'invoice_id': id,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            fileName = f'Invoice_{id}.pdf'
            content = f'inline; filename={fileName}'
            response['Content-Disposition'] = content
            return response
        return HttpResponse(pdf, content_type='application/pdf')
