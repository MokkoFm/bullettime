from django.shortcuts import render
from . models import Service
from . forms import CustomerForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):
    services = Service.objects.all()
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid:
            messages.success(request, 'Your message has been sent. Thank you!')
            form.save()
            return HttpResponseRedirect('')

    context = {
        "services": services,
        "form": form
    }
    return render(request, "index.html", context=context)
