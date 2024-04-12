from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
# from website.models import Contact
# from website.forms import NameForm, ContactForm, NewsletterForm
# from django.contrib import messages
# Create your views here.


def index_view(request) :
    return render(request, "website/index.html")

def about_view(request) :
    return render (request, "website/about.html")


def contact_view(request) :
    return render(request, "website/contact.html")


def newsletter_view(request) :
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email address submited successfully .')
            return HttpResponseRedirect('/')

    else :
        messages.add_message(request,messages.ERROR,'your email address did not submited successfully .')
        return HttpResponseRedirect('/')