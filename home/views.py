from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return to the index page """

    return render(request, 'home/index.html')


def contact_form(request):
    """ A view for contact form """

    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        messages.success(request, 'Thank you for contacting us')
    return render(request, 'home/contact.html')
