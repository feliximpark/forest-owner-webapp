from django.shortcuts import render
from django.views.generic import TemplateView
from leaflet.forms.widgets import LeafletWidget

# Create your views here.
class StartScreenView(TemplateView):
    template_name = 'forest_app/start_screen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map'] = LeafletWidget()
        return context
