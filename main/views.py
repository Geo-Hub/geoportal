from django.core import mail
from django.shortcuts import render
from .models import *
from .forms import LandRegistrationForm
from django.http import HttpResponseRedirect
from django.core.serializers import serialize
from chartit import DataPool, Chart


# Create your views here.
def home(request):
    title = 'Home'
    template = 'home.html'
    context = {'title': title}
    return render(request, template, context)


def about(request):
    title = 'About'
    template = 'about.html'
    context = {'title': title}
    return render(request, template, context)


def contact(request):
    title = 'Contact'
    helpmessage = None
    if request.method == 'POST':
        intention = request.POST.get("intention")
        if intention == "submit_form":
            showform = False
            name = request.POST.get("name_of_sender")
            email_address = request.POST.get("email_address")
            message = request.POST.get("message")

            mail.send_mail(
                "Feedback on Geohub Geoportal by "+name,
                message,
                email_address,
                ["mailappvictor@gmail.com", "jimmywainaina@gmail.com", "thomas.muteti@gmail.com", "njerimurage92@gmail.com", "nombumurage@gmail.com"],
                fail_silently=False
            )

            helpmessage = 'Thank you for your feedback.'
            context = {
                'title': title,
                'helpmessage': helpmessage,
                'showform': showform
            }
            return render(request, 'contact.html', context)
        else:
            helpmessage = 'Fill the form below'
            showform = True
            context = {
                'title': title,
                'helpmessage': helpmessage,
                'showform': showform
            }

            return render(request, 'contact.html', context)

    return render(request, 'contact.html', {})


def data(request):
    template = 'lookupdata.html'
    title = 'Shamba'
    shambas = serialize('geojson', Shamba.objects.all())
    counties = serialize('geojson', KiambuCounty.objects.all())
    constituencies = serialize('geojson', KiambuConstituencies.objects.all())

    context = {
        'title': title,
        'shambas': shambas,
        'counties': counties,
        'constituencies': constituencies
    }
    return render(request, template, context)


def registershamba(request):
    template = 'registershamba.html'
    title = 'Register'
    reg_form = LandRegistrationForm()
    context = {
        'title':title,
        'reg_form': reg_form
    }
    if request.method == 'POST':
        pass
    else:
        return render(request, template, context)

def update_payment(request):
    template = 'update-payment.html'
    shambas = Shamba.objects.all().order_by('-parcel_no')[:20]
    context = {
        'shambas':shambas
    }
    if request.method == "POST":
        post_type = request.POST.get('post-type')
        if post_type == "yearly-update":
            for shamba in Shamba.objects.all():
                try:
                    value = int(shamba.balance)
                    new_bal = value+100
                    shamba.balance = new_bal
                    shamba.save()
                except Exception:
                    shamba.balance = 100
                    shamba.save()
        elif post_type == "payment-update":
            arrears = request.POST.get('arrears-update')
            payment = request.POST.get('payment-update')
            shamba_id = request.POST.get('shamba-id')
            shamba_obj = Shamba.objects.get(id=int(shamba_id))   
            try:
                new_bal = int(shamba_obj.balance) # db has saved int value
            except Exception: # db has maybe none in db
                new_bal = 0
            if payment:
                new_bal -= int(payment)
            if arrears:
                new_bal += int(arrears)
            shamba_obj.balance = new_bal
            shamba_obj.save()
            
    return render(request, template, context)

def discardshamba(request):
    template = 'discardshamba.html'
    title = 'Discard'
    # shambas = OwnershipInfo.objects.all()
    context = {
        'title': title,
        # 'shambas':shambas,
    }
    return render(request, template, context)


def changeowner(request):
    template = 'changeowner.html'
    title = 'Change'
    context = {
        'title': title,
    }
    return render(request, template, context)


def statistics(request):
    template = 'statistics.html'
    title = 'Statistics'
    # Step 1: Create a DataPool with the data we want to retrieve.
    order_by = request.GET.get('order_by', 'id')
    data = Shamba.objects.all().order_by('id')
    context = {
        'title': title,
        'data': data
    }
    return render(request, template, context)
