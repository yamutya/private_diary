from django.views import generic

from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name="index.html"

class InquiryView(generic.FormView):
    template_name = "inquiery.html"
    form_class = InquiryForm