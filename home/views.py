from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from .forms import ContactForm
from products.models import Product
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "home/index.html"
# categories = Category.objects.filter(name__in=categories)

    def get_context_data(self, *args, **kwargs):
        shop_items = Product.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['shop_items'] = shop_items
        return context


class AboutView(TemplateView):
    template_name = "home/about.html"


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = "home/contact.html"

    def get_success_url(self):
        return reverse("contact")

    """" Getting clean data from the form and creating
        a message to get sent to default email"""

    def form_valid(self, form):
        messages.success(self.request,
                         "Thank you for getting in touch with us. We have received your message.")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
        Received message below from {name}, {email}
        ___________________________
        {message}

        """
        send_mail(
            subject="Message from Focus contact form",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_invalid(form)
