from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


# Create your views here.
class TestView(TemplateView):
    template_name = 'test.html'


class URLEndecView(TemplateView):
    template_name = 'urlendec.html'


class HexEndecView(TemplateView):
    template_name = 'hexendec.html'


class BinEndecView(TemplateView):
    template_name = 'binendec.html'


class OctEndecView(TemplateView):
    template_name = 'octendec.html'


class B64EndecView(TemplateView):
    template_name = 'b64endec.html'


class HashEndecView(TemplateView):
    template_name = 'hashendec.html'


class CSView(TemplateView):
    def get(self, request, *args, **kwargs):
        if kwargs['sheet_name'] == 'ascii':
            return render_to_response('sheets/asciisheet.html')
