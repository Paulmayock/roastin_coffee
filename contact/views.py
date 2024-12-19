from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Contact
from .forms import ContactForm


class CreateContact(SuccessMessageMixin, CreateView):
    """ Contact form view """
    template_name = 'contact/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = '/'
    success_message = "Your contact has been received"
