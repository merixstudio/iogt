from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView


def test(request, id=None):
    return render(request, '../home/templates/home/test.html', context={'id': id})


class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'

    def get_context_data(self, **kwargs):
        return {
            'test_url': reverse('test'),
        }
