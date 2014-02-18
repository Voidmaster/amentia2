from django.shortcuts import render
from django.views.generic.list import ListView
from myPage.apps.main.models import Client

def index_view(request):
    return render(request, 'main/index.html')

class ClientsView(ListView):

    model = Client
    template_name = 'main/clients.html'

    def get_context_data(self, **kwargs):
        context = super(ClientsView, self).get_context_data(**kwargs)
        context['latest_clients'] = Client.objects.all()[:5]
        return context

