from django.shortcuts import render
from . models import Service, Partner, Gallery
from . forms import CustomerForm
from django.contrib import messages
from django.views.decorators.cache import cache_page
from compression_middleware.decorators import compress_page


@compress_page
@cache_page(60 * 15)
def index(request):
    services = Service.objects.all()
    partners = Partner.objects.all()
    images = Gallery.objects.all()

    form = CustomerForm()
    messages.success(request, '')
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid:
            messages.success(request, 'Your message has been sent. Thank you!')
            form.save()
            form = CustomerForm()
            messages.success(request, '')

    context = {
        "services": services,
        "partners": partners,
        "images": images,
        "form": form
    }
    return render(request, "index.html", context=context)
