from django.views import generic


class Index(generic.TemplateView):
    template_name = 'index.html'

class Welcome(generic.TemplateView):
    template_name = 'welcome.html'

class Thanks(generic.TemplateView):
    template_name = 'thanks.html'